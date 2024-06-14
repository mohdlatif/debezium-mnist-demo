#!/usr/bin/env python3

# from urllib.request import urlretrieve

from diagrams import Cluster, Diagram
from diagrams.custom import Custom
from diagrams.generic.device import Mobile
from diagrams.onprem.database import Postgresql
from diagrams.onprem.queue import Kafka
from diagrams.programming.language import Cpp
from diagrams.programming.language import NodeJS
from diagrams.programming.language import Python


# # Download Debezim icon
# debezium_url = "https://design.jboss.org/debezium/logo/final/color/color_debezium_256px.png"
debezium_icon = "img/debezium.png"
# urlretrieve(debezium_url, debezium_icon)

# # Download TensorFlow icon
# tensorflow_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2d/Tensorflow_logo.svg/224px-Tensorflow_logo.svg.png"
tensorflow_icon = "img/tensorflow.png"
# urlretrieve(tensorflow_url, tensorflow_icon)

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

    with Cluster("Kafka Connect"):
        debezium = Custom("Debezium", debezium_icon)
        kafka = Kafka("Kafka")
        debezium >> kafka

    with Cluster("Python classifier"):
        python = Python("Python consumer/producer")
        tensorflow = Custom("TensorFlow", tensorflow_icon)
        python >> tensorflow
        tensorflow >> python

    node = NodeJS("Web app")
        
    qt >> Postgresql("Postgres") >> debezium
    kafka >> python
    python >> kafka
    kafka >> node
    node >> Mobile("User device")
