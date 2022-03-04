try:
 
    from enum import Enum
    from io import BytesIO, StringIO
    from typing import Union
 
    import pandas as pd
    import streamlit as st
except Exception as e:
    print(e)
 
STYLE = """
<style>
img {P
    max-width: 100%;
}
</style>
"""
 
 
class FileUpload(object):
 
    def __init__(self):
        self.fileTypes = ["csv", "png", "jpg"]
 
    def run(self):
        """
        Upload File on Streamlit Code
        :return:
        """
        st.info(__doc__)
        st.markdown(STYLE, unsafe_allow_html=True)
        file = st.file_uploader("Upload file", type=self.fileTypes)
        show_file = st.empty()
        if not file:
            show_file.info("Please upload a file of type: " + ", ".join(["csv", "png", "jpg"]))
            return
        content = file.getvalue()
        if isinstance(file, BytesIO):
            show_file.image(file)
        else:
            data = pd.read_csv(file)
            st.dataframe(data.head(10))
        file.close()
 
 
if __name__ ==  "__main__":
    helper = FileUpload()
    helper.run()