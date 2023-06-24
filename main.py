def is_palindrom(st):
    st = st.lower()
    st = st.replace(' ', '')
    if st[::-1] == st: return True
    else: return False