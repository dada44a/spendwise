import { InputHTMLAttributes } from "react";

interface InputProps extends InputHTMLAttributes<HTMLInputElement>{};

export default function Input({...props}:InputProps){
    return(
        <input {...props} className="input input-neutral w-full" />
    )
}