#!/usr/bin/env python3

# from urllib.request import urlretrieve

from diagrams import Cluster, Diagram
from diagrams.custom import Custom
from diagrams.onprem.database import Postgresql
from diagrams.programming.language import Cpp


## Download Qt icon
# qt_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/8/81/Qt_logo_neon_2022.svg/640px-Qt_logo_neon_2022.svg.png"
qt_icon = "img/qt.png"
# urlretrieve(qt_url, qt_icon)

graph_attr = {
     "bgcolor": "transparent",
}

with Diagram(show=False, graph_attr=graph_attr):

    with Cluster("Qt application"):
        qt = Custom("", qt_icon)
        cpp = Cpp("")

    qt >> Postgresql("Postgres")
    
