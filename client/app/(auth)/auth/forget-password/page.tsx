import React from "react";

export default function ForgotPassword() {
    return (
      <div className="flex items-center justify-center min-h-screen bg-gray-100">
        <div className="w-full max-w-md p-6 bg-white rounded-lg shadow-md">
          <h2 className="text-2xl font-semibold text-center text-gray-700 mb-4">
            Forgot Password
          </h2>
          <p className="text-gray-500 text-center mb-6">
            Enter your email to reset your password.
          </p>
          <form>
            <div className="mb-4">
              <label className="block text-gray-700">Email Address</label>
              <input
                type="email"
                placeholder="Enter your email"
                className="w-full px-4 py-2 mt-2 border rounded-lg focus:ring focus:ring-blue-300 focus:outline-none"
              />
            </div>
            <button
              type="submit"
              className="w-full px-4 py-2 text-white bg-blue-600 rounded-lg hover:bg-blue-700 focus:outline-none"
            >
              Reset Password
            </button>
          </form>
          <p className="mt-4 text-center text-gray-600">
            Remembered? <a href="/login" className="text-blue-600 hover:underline">Login</a>
          </p>
        </div>
      </div>
    );
  }
  