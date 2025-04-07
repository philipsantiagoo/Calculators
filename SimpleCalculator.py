import flet as ft
import math


def calculator(page: ft.Page):
    page.title = 'Calculator'
    page.bgcolor = "#2d2d2d"                                                   # cor
    page.window.width = 350                                                    # comprimento | largura
    page.window.height = 465                                                   # altura


    todos_valores = ''


    resultado_texto = ft.Text(value='0', size=28, color='white', text_align="right")


    def entrar_valores(valor):
        nonlocal todos_valores
        todos_valores += str(valor.control.text)
        resultado_texto.value = todos_valores
        page.update()
    

    def limpar_tela(valor):
        nonlocal todos_valores
        todos_valores = ''
        resultado_texto.value = '0'
        page.update()
    

    def backspace(valor):
        nonlocal todos_valores
        todos_valores = todos_valores[:-1]
        resultado_texto.value = todos_valores if todos_valores else '0'
        page.update()
    

    def calcular(valor):
        nonlocal todos_valores
        try:
            resultado_texto. value = str(eval(todos_valores))
            todos_valores = resultado_texto.value
        except:
            resultado_texto.value = 'Error'
            todos_valores = ''
        page.update()



    tela = ft.Container(
        content=resultado_texto,
        bgcolor="#37474F",                                                     # cor de fundo da tela de contas
        padding=10,                                                            # borda 
        border_radius=10,                                                      # arredondamento da borda
        height=70,                                                             # altura da borda
        alignment=ft.alignment.center_right                                    # alinhamento e centralização das operações anteriores (para a direita)
    )

    # Estilização dos botões
    estilo_numeros = {
        "height":60,
        "bgcolor":'#4d4d4d',
        "color":'white',
        "expand":1,
    }

    estilo_operadores = {
        "height":60,
        "bgcolor":'#FF9500',
        "color":'white',
        "expand":1,
    }

    estilo_limpar = {
        "height":60,
        "bgcolor":'#FF3B30',
        "color":'white',
        "expand":1,
    }

    estilo_igualdade = {
        "height":60,
        "bgcolor":'#34C759',
        "color":'white',
        "expand":1,
    }



    grelha_de_botoes = [                                                       # lista que contém outras listas que contém tuplas dos botões

        [
            ('C', estilo_limpar, limpar_tela),
            ('%', estilo_operadores, entrar_valores),
            ('/', estilo_operadores, entrar_valores),
            ('**', estilo_operadores, entrar_valores),
        ],

           [
            ('7', estilo_numeros, entrar_valores),
            ('8', estilo_numeros, entrar_valores),
            ('9', estilo_numeros, entrar_valores),
            ('-', estilo_operadores, entrar_valores),
        ],

           [
            ('4', estilo_numeros, entrar_valores),
            ('5', estilo_numeros, entrar_valores),
            ('6', estilo_numeros, entrar_valores),
            ('+', estilo_operadores, entrar_valores),
        ],

           [
            ('1', estilo_numeros, entrar_valores),
            ('2', estilo_numeros, entrar_valores),
            ('3', estilo_numeros, entrar_valores),
            ('*', estilo_operadores, entrar_valores),
        ],

           [
            ('0', {**estilo_numeros, "expand":1}, entrar_valores),
            ('.', estilo_numeros, entrar_valores),
            ('=', estilo_igualdade, calcular),
            ('⌫', estilo_limpar, backspace),
        ],

    ]


    botoes = []
    
    for linha in grelha_de_botoes:
        linha_control = []
        for texto, estilo, handler in linha:
            btn = ft.ElevatedButton(
                    text=texto,
                    on_click=handler,
                    **estilo,
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=5),
                        padding=0
                    )
                    
                 )
            linha_control.append(btn)
        botoes.append(ft.Row(linha_control, spacing=5))


    page.add(
        ft.Column(
            [
                tela,
                ft.Column(botoes, spacing=5)

            ]
        )
    )


ft.app(target=calculator)