import gradio as gr
from sample_project.hello import hello


def greet(name: str, intensity: str) -> str:
    return hello(name) + "!" * int(intensity)


demo = gr.Interface(
    fn=greet,
    inputs=["text", "slider"],
    outputs=["text"],
)

demo.launch()
