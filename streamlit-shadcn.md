Title: GitHub - ObservedObserver/streamlit-shadcn-ui: Using shadcn-ui components in streamlit

URL Source: http://github.com/ObservedObserver/streamlit-shadcn-ui

Markdown Content:
streamlit-shadcn-ui 🚧
----------------------

[](http://github.com/ObservedObserver/streamlit-shadcn-ui#streamlit-shadcn-ui-construction)

[![Image 29: PyPI - Version](https://camo.githubusercontent.com/813468f47ae2760bf1eafaeb7dfe98dd99431dcc4b3323c07f88f0a04e73c83f/68747470733a2f2f696d672e736869656c64732e696f2f707970692f762f73747265616d6c69742d73686164636e2d7569)](https://pypi.org/project/streamlit-shadcn-ui/) [![Image 30: PyPI - Downloads](https://camo.githubusercontent.com/2666a237c117a2f5b1ab37fc6af3429a520b2318ad6850ea18a52aa2a430f561/68747470733a2f2f696d672e736869656c64732e696f2f707970692f646d2f73747265616d6c69742d73686164636e2d7569)](https://camo.githubusercontent.com/2666a237c117a2f5b1ab37fc6af3429a520b2318ad6850ea18a52aa2a430f561/68747470733a2f2f696d672e736869656c64732e696f2f707970692f646d2f73747265616d6c69742d73686164636e2d7569) [![Image 31: Streamlit App](https://camo.githubusercontent.com/a68ac24f2cc7fb1ef422166946e1067437a861d1c4e6debbe1cf0fb5bd31d31a/68747470733a2f2f7374617469632e73747265616d6c69742e696f2f6261646765732f73747265616d6c69745f62616467655f626c61636b5f77686974652e737667)](https://shadcn.streamlit.app/)

Using shadcn-ui components in streamlit

[![Image 32: streamlit-shadcn](https://private-user-images.githubusercontent.com/22167673/285388396-75620347-9e9c-454c-a7ce-381d7464c519.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzMyNTU4MTIsIm5iZiI6MTczMzI1NTUxMiwicGF0aCI6Ii8yMjE2NzY3My8yODUzODgzOTYtNzU2MjAzNDctOWU5Yy00NTRjLWE3Y2UtMzgxZDc0NjRjNTE5LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDEyMDMlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQxMjAzVDE5NTE1MlomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWNhN2YyZjQ3NzQ4ZWNmMTIwYThjNzlkYjgxNmI1MTc4MDgzMjdiZTE0ZjliYjNiYTZkNmU2Mzc2MWI0NWEzZDUmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0._4SC8h7S2mMhJ3kauZVZjufQsDno5xx3eMOl1DaRuJI)](https://private-user-images.githubusercontent.com/22167673/285388396-75620347-9e9c-454c-a7ce-381d7464c519.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzMyNTU4MTIsIm5iZiI6MTczMzI1NTUxMiwicGF0aCI6Ii8yMjE2NzY3My8yODUzODgzOTYtNzU2MjAzNDctOWU5Yy00NTRjLWE3Y2UtMzgxZDc0NjRjNTE5LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDEyMDMlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQxMjAzVDE5NTE1MlomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWNhN2YyZjQ3NzQ4ZWNmMTIwYThjNzlkYjgxNmI1MTc4MDgzMjdiZTE0ZjliYjNiYTZkNmU2Mzc2MWI0NWEzZDUmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0._4SC8h7S2mMhJ3kauZVZjufQsDno5xx3eMOl1DaRuJI)

Installation
------------

[](http://github.com/ObservedObserver/streamlit-shadcn-ui#installation)

pip install streamlit-shadcn-ui

example:

import streamlit\_shadcn\_ui as ui
trigger\_btn \= ui.button(text\="Trigger Button", key\="trigger\_btn")

ui.alert\_dialog(show\=trigger\_btn, title\="Alert Dialog", description\="This is an alert dialog", confirm\_label\="OK", cancel\_label\="Cancel", key\="alert\_dialog1")

Components
----------

[](http://github.com/ObservedObserver/streamlit-shadcn-ui#components)

Check docs and compoenent examples in [![Image 33: Streamlit App](https://camo.githubusercontent.com/a68ac24f2cc7fb1ef422166946e1067437a861d1c4e6debbe1cf0fb5bd31d31a/68747470733a2f2f7374617469632e73747265616d6c69742e696f2f6261646765732f73747265616d6c69745f62616467655f626c61636b5f77686974652e737667)](https://shadcn.streamlit.app/)

*   button
*   checkbox
*   select
*   tabs
*   card
*   avatar
*   date\_picker
*   date\_range\_picker (date\_picker with mode="range")
*   table
*   input
*   slider
*   textarea
*   switch
*   radio\_group
*   alert\_dialog
*   hover\_card
*   badges
*   link\_button

[![Image 34: streamlit card](https://private-user-images.githubusercontent.com/22167673/286415344-799b9235-96a6-406e-b270-e685de9ba5fd.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzMyNTU4MTIsIm5iZiI6MTczMzI1NTUxMiwicGF0aCI6Ii8yMjE2NzY3My8yODY0MTUzNDQtNzk5YjkyMzUtOTZhNi00MDZlLWIyNzAtZTY4NWRlOWJhNWZkLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDEyMDMlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQxMjAzVDE5NTE1MlomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTgyNzkyZWYyODhjOTk1MDNkZDZmYmU1YzdkZWM1NDkzMGYwNmJlNWQ2N2EyNzM3ZjAyZGVkMmMzMjY2NDIxZjUmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.T2T-Fl_Myr0JL1_hY2JCfNci0T53B3pXPuQ_qIa1KX8)](https://private-user-images.githubusercontent.com/22167673/286415344-799b9235-96a6-406e-b270-e685de9ba5fd.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzMyNTU4MTIsIm5iZiI6MTczMzI1NTUxMiwicGF0aCI6Ii8yMjE2NzY3My8yODY0MTUzNDQtNzk5YjkyMzUtOTZhNi00MDZlLWIyNzAtZTY4NWRlOWJhNWZkLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDEyMDMlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQxMjAzVDE5NTE1MlomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTgyNzkyZWYyODhjOTk1MDNkZDZmYmU1YzdkZWM1NDkzMGYwNmJlNWQ2N2EyNzM3ZjAyZGVkMmMzMjY2NDIxZjUmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.T2T-Fl_Myr0JL1_hY2JCfNci0T53B3pXPuQ_qIa1KX8)

[![Image 35: streamlit date picker](https://private-user-images.githubusercontent.com/22167673/286415667-8c32c4e0-8aaf-421d-b459-bceb63f1dd0a.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzMyNTU4MTIsIm5iZiI6MTczMzI1NTUxMiwicGF0aCI6Ii8yMjE2NzY3My8yODY0MTU2NjctOGMzMmM0ZTAtOGFhZi00MjFkLWI0NTktYmNlYjYzZjFkZDBhLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDEyMDMlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQxMjAzVDE5NTE1MlomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTRmMzg2MWViNTcyMjRlYTY4M2NkNmZiZTM5YmZkZjg4MjFhZjZmZGVhMWIxMjZiNmM1N2ZkNzM4ZjI2ZjAzNTUmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.74G1mBB9RvdKq2zcE6IhxrwgWeoajTZgGZeiCK2gvAU)](https://private-user-images.githubusercontent.com/22167673/286415667-8c32c4e0-8aaf-421d-b459-bceb63f1dd0a.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzMyNTU4MTIsIm5iZiI6MTczMzI1NTUxMiwicGF0aCI6Ii8yMjE2NzY3My8yODY0MTU2NjctOGMzMmM0ZTAtOGFhZi00MjFkLWI0NTktYmNlYjYzZjFkZDBhLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDEyMDMlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQxMjAzVDE5NTE1MlomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTRmMzg2MWViNTcyMjRlYTY4M2NkNmZiZTM5YmZkZjg4MjFhZjZmZGVhMWIxMjZiNmM1N2ZkNzM4ZjI2ZjAzNTUmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.74G1mBB9RvdKq2zcE6IhxrwgWeoajTZgGZeiCK2gvAU)

[![Image 36: streamlit select](https://private-user-images.githubusercontent.com/22167673/286416118-f5a6eb8d-163f-4a7b-b88b-9b962d32dc1b.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzMyNTU4MTIsIm5iZiI6MTczMzI1NTUxMiwicGF0aCI6Ii8yMjE2NzY3My8yODY0MTYxMTgtZjVhNmViOGQtMTYzZi00YTdiLWI4OGItOWI5NjJkMzJkYzFiLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDEyMDMlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQxMjAzVDE5NTE1MlomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTYyN2JhYjZlZTRkOWMxYTQwNzA1MzlkNzljOTY0MWVjYmM0ODA3YzQyMDg2MTgyYjEyODg3ZTdjODAwZjAyN2QmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.uiRmvGIH1R1MFc4Vu4sBlk_5uX0IxmXxmVK_3RD9rTY)](https://private-user-images.githubusercontent.com/22167673/286416118-f5a6eb8d-163f-4a7b-b88b-9b962d32dc1b.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzMyNTU4MTIsIm5iZiI6MTczMzI1NTUxMiwicGF0aCI6Ii8yMjE2NzY3My8yODY0MTYxMTgtZjVhNmViOGQtMTYzZi00YTdiLWI4OGItOWI5NjJkMzJkYzFiLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDEyMDMlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQxMjAzVDE5NTE1MlomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTYyN2JhYjZlZTRkOWMxYTQwNzA1MzlkNzljOTY0MWVjYmM0ODA3YzQyMDg2MTgyYjEyODg3ZTdjODAwZjAyN2QmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.uiRmvGIH1R1MFc4Vu4sBlk_5uX0IxmXxmVK_3RD9rTY)

One more thing
--------------

[](http://github.com/ObservedObserver/streamlit-shadcn-ui#one-more-thing)

There is a new component in testing, it will allows you to nest all streamlit-shadcn-ui components together. It will not treat each component as an independent streamlit custom component in iframe, but parse the component structure as data and render them all at once in one iframe.

example ([live demo](https://shadcn.streamlit.app/Experiment(Cool))):

with ui.card(key\="card1"):
    with ui.card(key\="card2"):
        ui.element("input", key\="card2\_input")
        ui.element("button", key\="card2\_btn", text\="Nest Submmit", variant\="outline")
    ui.element("button", key\="card1\_btn", text\="Hello World")

[![Image 37: streamlit react_component](https://private-user-images.githubusercontent.com/22167673/286416327-ab40ed25-cc41-4630-adc9-7d604e44d538.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzMyNTU4MTIsIm5iZiI6MTczMzI1NTUxMiwicGF0aCI6Ii8yMjE2NzY3My8yODY0MTYzMjctYWI0MGVkMjUtY2M0MS00NjMwLWFkYzktN2Q2MDRlNDRkNTM4LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDEyMDMlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQxMjAzVDE5NTE1MlomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWVmM2ZlMDY0NWNlZjYwZDJhOWZhODUwZGJjZDQ0NTM3ZTIxZmQyYmQzZTZhMzE3ZGRmYzRhZTkxODU5MGQ4NGYmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.6RBkm34y-SmRWn5dgKJHM-fB-Mvh5eyv2NAEtWxlKyM)](https://private-user-images.githubusercontent.com/22167673/286416327-ab40ed25-cc41-4630-adc9-7d604e44d538.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzMyNTU4MTIsIm5iZiI6MTczMzI1NTUxMiwicGF0aCI6Ii8yMjE2NzY3My8yODY0MTYzMjctYWI0MGVkMjUtY2M0MS00NjMwLWFkYzktN2Q2MDRlNDRkNTM4LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDEyMDMlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQxMjAzVDE5NTE1MlomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWVmM2ZlMDY0NWNlZjYwZDJhOWZhODUwZGJjZDQ0NTM3ZTIxZmQyYmQzZTZhMzE3ZGRmYzRhZTkxODU5MGQ4NGYmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.6RBkm34y-SmRWn5dgKJHM-fB-Mvh5eyv2NAEtWxlKyM)

Development Guide
-----------------

[](http://github.com/ObservedObserver/streamlit-shadcn-ui#development-guide)

There are several scripts in `scripts` folder to help you develop this project.

# For local development
./scripts/frontend.sh # frontend dev server
./scripts/dev.sh # streamlit dev server

This repo follows the streamlit custom component structure.

*   `./streamlit_shadcn_ui` is the python package
    *   `./streamlit_shadcn_ui/components` is the frontend mono repo
        *   `./streamlit_shadcn_ui/components/packages/frontend` is the custom components collection.
        *   `./streamlit_shadcn_ui/components/packages/streamlit-components-lib` is a patch of streamlit-components-lib for react 18 (For now, only the react/react-dom version is changed).
    *   `./streamlit_shadcn_ui/py_components` is the python level API for components.

Reference
---------

[](http://github.com/ObservedObserver/streamlit-shadcn-ui#reference)

*   [streamlit-shadcn-ui examples and docs repo](https://github.com/ObservedObserver/steamlit-shadcn-ui-docs)
*   [Streamlit](https://streamlit.io/)
*   [shadcn-ui](https://ui.shadcn.com/)

License
-------

[](http://github.com/ObservedObserver/streamlit-shadcn-ui#license)

This repo is under MIT license. See [LICENSE](https://github.com/ObservedObserver/streamlit-shadcn-ui/blob/main/LICENSE) for details. `streamlit_shadcn_ui/components/packages/streamlit-components-lib` is under its original Apache-2.0 license. It is a temporal patch for streamlit-components-lib in react 18.