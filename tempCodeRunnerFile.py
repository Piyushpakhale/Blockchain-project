remember_me_var = tk.BooleanVar()
check_remember_me = tk.Checkbutton(root, text="remember me                      ", variable=remember_me_var, bg='#5D5D5D', fg='white',
                                   font=("Arial", 14))
check_remember_me.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

# Accept Terms & Conditions Checkbox
terms_var = tk.BooleanVar()
check_terms = tk.Checkbutton(root, text="Accept Terms & Conditions", variable=terms_var, bg='#5D5D5D', fg='white',
                             font=("Arial", 14))
check_terms.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

# Log In Button
login_button = tk.Button(root, text="Login!", command=login, bg='#390ACA', fg='white', font=(
        "Arial", 17))
login_button.grid(row=5, column=1, padx=30, pady=20)
    
# Sign Up Button
sign_up_button = tk.Button(root, text="Sign Up?", command=sign_up, bg='#390ACA', fg='white', font=("Arial", 16))
sign_up_button.grid(row=5, column=0, padx=10, pady=60)
