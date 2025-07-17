if __name__ == '__main__':
    s = input()
    
    print(any([st.isalnum() for st in s]))
    print(any([st.isalpha() for st in s]))
    print(any([st.isdigit() for st in s]))
    print(any([st.islower() for st in s]))
    print(any([st.isupper() for st in s]))