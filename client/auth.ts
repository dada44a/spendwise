import NextAuth from "next-auth"
import Credentials from "next-auth/providers/credentials"
import { PrismaClient } from "@prisma/client"
import { redirect } from "next/navigation"
import bcrypt from "bcryptjs"
const prisma = new PrismaClient()

const getUserFromDb = async (email: string, pwHash: string) => {
    const user = await prisma.user.findUnique({
        where: { email },
    })
    if (!user) return null
    const isPasswordValid = await bcrypt.compare(pwHash, user.password)
    if (!isPasswordValid) return null
    return user
}

export const { handlers, signIn, signOut, auth } = NextAuth({
    providers: [
        Credentials({
            credentials: {
                email: { label: "Email", type: "email" },
                password: { label: "Password", type: "password" },
            },
            authorize: async (credentials) => {
                const email = credentials.email as string
                const password = credentials.password as string
                const pwHash = await bcrypt.hash(password, 10)

                const user = await getUserFromDb(email, pwHash)

                if (!user) {
                    throw new Error("Invalid credentials.")
                }
                console.log("User logged in successfully.")
                redirect("/")
            }
        })

    ],
})