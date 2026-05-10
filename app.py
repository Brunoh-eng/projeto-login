import customtkinter as ctk

ctk.set_appearance_mode('dark')

def validar_login():
    if campo_usuario.get() == 'Bruno' and campo_senha.get() == '123456':
        resultado_login.configure(text='Login feito com sucesso!', text_color='green')
    else:
        resultado_login.configure(text='Senha incorreta', text_color='red')

app = ctk.CTk()
app.title('Sistema de Login')
app.geometry('300x280')

label_usuario = ctk.CTkLabel(app, text='Usuário')
label_usuario.pack(pady=10)

campo_usuario = ctk.CTkEntry(app, placeholder_text='Digite seu usuário')
campo_usuario.pack(pady=10)

label_senha = ctk.CTkLabel(app, text='Senha')
label_senha.pack(pady=10)

campo_senha = ctk.CTkEntry(app, placeholder_text='Digite sua senha', show='*')
campo_senha.pack(pady=10)

botao_login = ctk.CTkButton(app, 
text='Login', 
fg_color='#1E90FF', hover_color="#0F4C96", 
command=validar_login)

botao_login.pack(pady=10)

resultado_login = ctk.CTkLabel(app, text=' ')
resultado_login.pack(pady=5)

lembre_me = ctk.CTkCheckBox(app, text='Lembre de mim')
lembre_me.pack(
    pady=5)

app.mainloop()