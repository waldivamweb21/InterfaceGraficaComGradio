import gradio as gr
import math



def fatorial(num):
    if num < 0:
        return "Fatorial não definido para numeros negativos"
    return math.factorial(num)

#print(fatorial(5))
iface = gr.Interface(
    fn=fatorial,
    inputs="number",
    outputs="text",
    title="Calculadora Fatorial",
    description="Insira um número para obter o fatorial."
)

iface.launch()
    