def check_code(code):
    warnings = []
    
    if "password" in code:
        warnings.append("⚠️ Hardcoded password found")
    if "eval(" in code:
        warnings.append("⚠️ Use of eval() is dangerous")
        
    return warnings


if __name__ == "__main__":
    user_code = input("Paste your code: ")
    results = check_code(user_code)
    
    if results:
        print("\nWarnings:")
        for r in results:
            print("-", r)
    else:
        print("✅ No obvious issues found")
