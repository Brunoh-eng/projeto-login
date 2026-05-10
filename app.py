import customtkinter as ctk

ctk.set_appearance_mode('dark')

def alternar_senha(): 
    if campo_senha.cget('show') == '*':
        campo_senha.configure(show='')
    else:
        campo_senha.configure(show='*')

def validar_login():
    if campo_usuario.get() == 'Bruno' and campo_senha.get() == '123456':
        resultado_login.configure(text='Login feito com sucesso!', text_color='green')
    else:
        resultado_login.configure(text='Senha incorreta', text_color='red')

tentativas = 0

def validar_login():
    global tentativas
    
    if campo_usuario.get() == 'Bruno' and campo_senha.get() == '123456':
        resultado_login.configure(text='Login feito com sucesso!', text_color='green')
        tentativas = 0
    else:
        tentativas += 1
        if tentativas >= 3:
            resultado_login.configure(text='Muitas tentativas! Tente mais tarde.', text_color='red')
            botao_login.configure(state='disabled')
        else:
            resultado_login.configure(text='Senha incorreta', text_color='red')

        
app = ctk.CTk()
app.title('Sistema de Login')
app.geometry('300x320')
app.attributes('-topmost', True)

label_title = ctk.CTkLabel(app, text='Seja bem-vindo!', font=('Arial', 16, 'bold'))
label_title.pack(pady=(15, 5))

label_usuario = ctk.CTkLabel(app, text='Usuário')
label_usuario.pack(pady=(10, 0))

campo_usuario = ctk.CTkEntry(app, placeholder_text='Digite seu usuário')
campo_usuario.pack(pady=(0, 0))

label_senha = ctk.CTkLabel(app, text='Senha')
label_senha.pack(pady=(10, 0))

# frame senha
frame_senha = ctk.CTkFrame(app, fg_color='transparent')
frame_senha.pack(pady=(0, 0))

campo_senha = ctk.CTkEntry(frame_senha, placeholder_text='Digite sua senha', show='*')
campo_senha.pack(side='left')

botao_olho = ctk.CTkButton(frame_senha, text='👁', width=30, command=alternar_senha)
botao_olho.pack(side='left', padx=(5, 0))

botao_login = ctk.CTkButton(app, text='Login', fg_color='#1E90FF', hover_color='#0F4C96', command=validar_login)
botao_login.pack(pady=16, padx=10)

resultado_login = ctk.CTkLabel(app, text=' ')
resultado_login.pack(pady=0)

lembre_me = ctk.CTkCheckBox(app, text='Lembre de mim')
lembre_me.pack(pady=0, padx=10)

Label_esqueci_senha = ctk.CTkLabel(app, text='esqueci minha senha', text_color='white', cursor='hand1', font=('Arial', 11, 'underline'))
Label_esqueci_senha.pack(pady=5)

app.mainloop()