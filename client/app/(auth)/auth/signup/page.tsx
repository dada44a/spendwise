import Button from "@/components/ui/Button";
import Input from "@/components/ui/Input";
import React from "react";

export default function SignUp() {
  return (
    <div className="flex h-screen w-full items-center justify-center">
      <div className="card card-border bg-base-100 w-96">
        <div className="card-body">
          <h2 className="card-title font-semibold text-[25px]">Sign Up</h2>
          <p>Enter the details below to sign up.</p>
          <div className="card-actions mt-5">
            <form className="flex flex-col gap-5 w-full">
              <label htmlFor="name" className="w-full">
                
                <Input type="text" placeholder="Name" name="name"/>
                
              </label>
              <label htmlFor="email">
                Email
                <Input type="email" id="email" placeholder="Email" name="email" />
              </label>
              <label htmlFor="password">
                Password
                <Input type="password" id="password" placeholder="Password" name="password" />
              </label>
              <label htmlFor="confirmPassword">
                Confirm Password
                <Input type="password" id="confirmPassword" placeholder="Confirm Password" name="confirmPassword" />
              </label>

              <Button type="submit" className="btn btn-primary">Sign Up</Button>

            </form>
            <p className="text-center">Go to Login Page.</p>
          </div>

        </div>
      </div>
    </div>
  );
}
