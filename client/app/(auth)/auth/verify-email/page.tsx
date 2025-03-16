import React from 'react'

const VerifyEmailPage = () => {
  return (
    <div className="min-h-screen bg-gray-100 py-6 flex flex-col justify-center sm:py-12">
      <div className="py-3 sm:max-w-xl sm:mx-auto">
        <div className="bg-white shadow-lg min-h-full rounded-lg overflow-hidden">
          <div className="px-4 py-8 sm:p-6">
            <div className="text-center">
              <h2 className="text-3xl font-bold leading-9 text-gray-900">
                Verify your email address
              </h2>
              <p className="mt-2 text-sm leading-5 text-gray-600">
                We've sent you an email with a verification link. Please click
                the link to verify your email address.
              </p>
            </div>
            <form className="mt-8 space-y-6" action="#" method="POST">
              <div>
                <label
                  htmlFor="email"
                  className="block text-sm font-medium leading-5 text-gray-700"
                >
                  Email
                </label>
                <div className="mt-1 rounded-md shadow-sm">
                  <input
                    id="email"
                    type="email"
                    required
                    className="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md placeholder-gray-400 focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm sm:leading-5"
                  />
                </div>
              </div>
              <div>
                <span className="block w-full rounded-md shadow-sm">
                  <button
                    type="submit"
                    className="w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-blue-600 hover:bg-blue-500 focus:outline-none focus:border-blue-700 focus:shadow-outline-blue active:bg-blue-700 transition duration-150 ease-in-out"
                  >
                    Resend verification email
                  </button>
                </span>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  )
}

export default VerifyEmailPage
