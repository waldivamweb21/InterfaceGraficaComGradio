import gradio as gr 

def reverter_texto(texto):
    texto_revertido = texto[::-1]
    return texto_revertido, len(texto_revertido)

#print(reverter_texto("Hello world!"))

iface = gr.Interface(
    fn=reverter_texto,
    inputs="text",
    outputs=["text", "number"],
    title="reversor de texto",
    description = "Insira um texto para reverte-lo e contar caracteres"
)

iface.launch()
