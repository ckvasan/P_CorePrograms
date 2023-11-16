def reverse_sentence(stmt :str):
    stripstmt = stmt.strip()

    words = [e for e in stripstmt.split(" ") if e != '']
    print(words)
    return " ".join(words[::-1])

result = reverse_sentence("Hello World")
print (result)
result2 = reverse_sentence("   The quick brown fox   jumps over the lazy dog   ")
result3 = reverse_sentence("One   two three  four   ")
result4 = reverse_sentence("    ")
print (result2)
print (result3)
print (result4)