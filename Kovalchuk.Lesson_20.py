import sqlite3
conn = sqlite3.connect('2022-05-10.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS book
(book_id INTEGER PRIMARY KEY AUTOINCREMENT, title VARCHAR(50), author VARCHAR(30), price DECIMAL(8, 2), 
amount INTEGER)''')
conn.commit()
a = 'Username & all symbols: !$%^&* END'
b = 'Surname & all symbols: ∫ ∬ ∭ ∮ ∯ ∰ ∱ ∲ ∳ ∃ ∄ ∅ ∆ ∇ ∈ ∉ ∊ ∋ ∌ ∍ ∎ ∏ ∐ ∑ − ' \
    '∓ ∔ ≳ ≴ ≵ ≶ ≷ ≸ ≹ ≺ ≻ ≼ ≽ ≾ ≿ ⊀ ⊁ ⊂ ⊃ ⊄ ⊅ ⊆ ⊇ ⊈ ⊉ ⊊ ⊋ ⊌ ⊍ ⊎ ⊏ ⊐ ⊑ ⊒ ⊓ ⊔ ⊕ ⊖ ' \
    '⊗ ⊘ ⊙ ⊚ ⊛ ⊜ ⊝ ⊞ ⊟ ⊠ ⊡ ⊢ ⊣ ⊤ ⊥ ⊦ ⊧ ⊨ ⊩ ⊪ ⊫ ⊬ ⊭ ⊮ ⊯ ⊰ ⊱ ⊲ ⊳ ⊴ ⊵ ⊶ ⊷ ⊸ ⊹ ⊺ ⊻ ⊼ ' \
    '⊽ ⊾ ⊿ ⋀ ⋁ ⋂ ⋃ ⋄ ⋅ ⋆ ⋇ ⋈ ⋉ ⋊ ⋋ ⋌ ⋍ ⋎ ⋏ ⋐ ⋑ ⋒ ⋓ ⋔ ⋕ ⋖ ⋗ ⋘ ⋙ ⋚ ⋛ ⋜ ⋝ ⋞ ⋟ ⋠ ⋡ ⋢ ⋣ ' \
    '⋤ ⋥ ⋦ ⋧ ⋨ ⋩ ⋪ ⋫ ⋬ ⋭ ⋮ ⋯ ⋰ ⋱ ⋲ ⋳ ⋴ ⋵ ⋶ ⋷ ⋸ ⋹ ⋺ ⋻ ⋼ ⋽ ⋾ ⋿ ✕ ✖ ✚  ∕ ∖ ∗ ∘ ∙ √ ∛ ∜ ∝ ' \
    '∟ ∠ ∡ ∢ ∣ ∤ ∥ ∦ ∧ ∨ ∩ ∪ ∴ ∵ ∶ ∷ ∸ ∹ ∺ ∻ ∼ ∽ ∾ ∿ ≀ ≁ ≂ ≃ ≄ ≅ ≆ ≇ ≈ ≉ ≊ ≋ ≌ ≍ ≎ ≏ ≐ ≑ ≒ ' \
    '≓ ≔ ≕ ≖ ≗ ≘ ≙ ≚ ≛ ≜ ≝ ≞ ≟ ≠ ≡ ≢ ≣ ≤ ≥ ≦ ≧ ≨ ≩ ≪ ≫ ≬ ≭ ≮ ≯ ≰ ≱ ≲ END' #не обрезает строку до 30 символов
c = 1234567891011.9120   #почему тип DECIMAL с ограничением (8, 2), а всё равно помещает в базу значение с большим кол-вом цифр????
d = 987654321.123        #почему тип INTEGER, а всё равно помещает в базу значение с запятой????
cursor.execute('''INSERT INTO book(title, author, price, amount) VALUES (?,?,?,?)''', (a, b, c, d))
conn.commit()
cursor.execute('''SELECT * FROM book''')
print(*cursor)
