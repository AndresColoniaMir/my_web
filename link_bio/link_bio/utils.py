import reflex as rx
# Comun

def lang() -> rx.Component:
    return rx.script("document.documentElement.lang='es'")

preview = "https://andrescolonia.com/assets/preview.png"
_meta=[
        {"name": "og:type", "content": "website"},
        {"name": "og:image", "content": preview},
        {"name": "twitter:card", "content": "summary_large_image"},
    ]

# Index

index_title = "Andrés Colonia - Desarrollador de Software"
index_description = "Conoce a Andrés Colonia, desarrollador de software con experiencia en Java, Python, Android y más."


index_meta = [
    {"name": "og:title", "content": index_title},
    {"name": "og:description", "content": index_description},
]
index_meta.extend(_meta)


