import streamlit as st

st.title("Hallo HSLU 👋")
st.write("Wenn du das siehst, funktioniert Streamlit korrekt!")

## Version mit Datei vom Internet
# from streamlit.components.v1 import html

# st.set_page_config(page_title="3D Modell Viewer", layout="centered")
# st.title("🧱 3D Viewer mit <model-viewer> in Streamlit")

# # Beispiel-GLB-Datei (kann lokal oder im Web liegen)
# #glb_url = "starbucks-disposable-cup/source/sitarbuckss.glb"
# # glb_url = r"C:\Users\manue\OneDrive\VS_Projects\DT_Programmieren\starbucks-disposable-cup\source\sitarbuckss.glb"
# glb_url = "https://modelviewer.dev/shared-assets/models/Astronaut.glb"

# # HTML für den Viewer
# viewer_html = f"""
#     <model-viewer
#         src="{glb_url}"
#         alt="3D Modell"
#         camera-controls
#         auto-rotate
#         exposure="0.8"
#         style="width: 100%; height: 500px; background-color: #f0f0f0;"
#         ar
#         ar-modes="webxr scene-viewer quick-look">
#     </model-viewer>

#     <!-- model-viewer Script -->
#     <script type="module"
#         src="https://ajax.googleapis.com/ajax/libs/model-viewer/3.4.0/model-viewer.min.js">
#     </script>
# """

# # In Streamlit einbetten
# html(viewer_html, height=550)


## Version mit Drag&Drop
# import base64
# import streamlit as st
# from streamlit.components.v1 import html

# st.title("🧱 3D Viewer – Lokale GLB-Datei")

# uploaded = st.file_uploader("Bitte GLB-Datei hochladen", type=["glb"])

# if uploaded:
#     glb_bytes = uploaded.read()
#     b64 = base64.b64encode(glb_bytes).decode("ascii")
#     data_url = f"data:model/gltf-binary;base64,{b64}"

#     viewer_html = f"""
#       <model-viewer
#           src="{data_url}"
#           alt="Lokales 3D Modell"
#           camera-controls
#           auto-rotate
#           style="width:100%;height:500px;background:#f0f0f0;">
#       </model-viewer>
#       <script type="module"
#         src="https://ajax.googleapis.com/ajax/libs/model-viewer/3.4.0/model-viewer.min.js">
#       </script>
#     """
#     html(viewer_html, height=550, scrolling=False)
# else:
#     st.info("Bitte eine .glb-Datei hochladen.")

import base64
import streamlit as st
from streamlit.components.v1 import html
import os

st.set_page_config(page_title="3D Viewer", layout="centered")
st.title("🧱 Automatischer 3D Viewer – lokale GLB-Datei")

# ---------------------------------------------------------
# 1️⃣ Pfad zur GLB-Datei (bitte anpassen)
glb_path = r"C:\Users\manue\OneDrive\VS_Projects\DT_Programmieren\starbucks-disposable-cup\source\sitarbuckss.glb"

# Prüfen, ob Datei vorhanden ist
if not os.path.exists(glb_path):
    st.error(f"Datei nicht gefunden:\n{glb_path}")
else:
    # ---------------------------------------------------------
    # 2️⃣ Datei einlesen und Base64-kodieren
    with open(glb_path, "rb") as f:
        glb_bytes = f.read()
    b64 = base64.b64encode(glb_bytes).decode("ascii")

    # 3️⃣ Data-URL erstellen (Browser kann direkt rendern)
    data_url = f"data:model/gltf-binary;base64,{b64}"

    # ---------------------------------------------------------
    # 4️⃣ HTML-Viewer einbetten
    viewer_html = f"""
      <model-viewer
          src="{data_url}"
          alt="Lokales 3D Modell"
          camera-controls
          auto-rotate
          style="width:100%;height:500px;background:#f0f0f0;">
      </model-viewer>

      <script type="module"
        src="https://ajax.googleapis.com/ajax/libs/model-viewer/3.4.0/model-viewer.min.js">
      </script>
    """
    html(viewer_html, height=550, scrolling=False)
