# Traffic-Forecasting-using-Air-Pollution-Data

Description

A system integrating traffic and atmospheric data from sensors with LSTM models to forecast traffic conditions and optimize air quality management, envisioned for smart city infrastructures.

Introduction

Living in London, we've first hand experienced the frustration of congestion. Hours spent in standstill traffic, with engines idling, release copious greenhouse gases into the air, becoming a routine part of our lives. This project designs a system to manage traffic and optimize air quality by integrating real-time data from sensors placed at congested junctions. A comprehensive approach to developing a cost-effective, accurate system for measuring air pollution and analyzing its relationship with traffic conditions is presented. The system integrates multiple components, including sensors that detect temperature, humidity, PM2.5, CO2, CO, volatile gases, NO2, and methane, alongside a camera unit to monitor traffic. By combining air quality data with real-time traffic monitoring through machine learning models, we can better understand the correlation between traffic and pollution levels. Additionally, the project explores the predictive potential of air pollution data. We developed an LSTM deep learning model to forecast future traffic conditions based on historical pollution data, demonstrating how air quality measurements can serve as proxies for predicting traffic patterns. The system offers valuable insights for urban traffic management and air quality control.

Methodology

1. Data Collection: Traffic conditions and environmental data are periodically gathered from camera units, pollution sensors, and other hardware deployed at key traffic junctions.

2. Data Preprocessing: The raw sensor data is cleaned, normalized, and structured for use in machine learning models. This includes time-series data on pollution levels and traffic density.

3. Modeling: An LSTM model is implemented to forecast future traffic conditions based on historical data. This model integrates environmental variables, such as air quality readings, to assess the traffic’s impact on pollution.

4. Optimization Algorithms: The system feeds the model’s predictions into optimization algorithms that dynamically adjust traffic signals and reroute vehicles to alleviate congestion and minimize air pollution.

5. Deployment: The real-time system can be deployed in urban areas, acting as an intermediary between traffic control units and smart city systems, to reduce congestion and improve air quality.

Sensors

The air quality monitoring system was designed to measure various pollutants and environmental factors, including PM2.5, CO2, CO, volatile gases, NO2, methane, and temperature-humidity. These pollutants have been selected because they are known to produce several adverse effects to human health and the environment. Particularly, PM2.5 and NO2 are associated with respiratory and cardiovascular diseases, while CO2 and methane contribute to greenhouse gas emissions and climate change. The sensors were assembled using an ESP-32 microcontroller coupled with different sensor modules sensing specific pollutants. The sensor network was constructed using Arduino-compatible hardware programmed with Micro Python. Each of the sensors was mounted on an ESP-32 board that served as a central controller, transmitting data to the central server via an MQTT client. The system was set to provide real-time data at every 15 minutes to ensure that traffic and pollution level variations remain meaningful without causing an overload of the sensor system. 

Datasets

Air Quality Dataset: Readings of temperature, noise, humidity, PM2.5, CO2, CO, volatile gases, NO2, and methane over a 3 day period at a junction in Kingston upon Thames, London were collected over a 3 day period in August 2023.

Local Vehicle Detection: A dataset consisting of 263 vehicular traffic images was collected using a camera placed at the junction in Kingston upon Thames, London, where the sensors were deployed locally. The dataset was manually annotated, labeling vehicles as cars, buses, or trucks. It was then split into training (70.3%), validation (19.8%), and test (9.9%) sets. This annotated dataset served as the foundation for training the traffic detection model.

Traffic Forecasting Dataset: This traffic forecasting dataset was chosen was due to its accurate temporal and spatial characteristics, which are ideal for modeling traffic patterns accurately. With data collected at 36 sensor locations along two major highways in Northern Virginia/Washington D.C., the dataset provides a comprehensive representation of real-world traffic conditions. Traffic volume was recorded every 15 minutes, ensuring sufficient temporal granularity to capture fluctuations in traffic flow, while the inclusion of 47 features—such as historical traffic volume, weekday, hour of the day, road direction, number of lanes, and road names—allowed for a detailed analysis of traffic dynamics.  The dataset was then divided into training and testing datasets: 1261 quarter-hours for training and 840 quarter-hours for testing. The diversity of features, combined with the spatial distribution of sensors, allowed the model to consider both local and regional traffic patterns, which made this dataset especially suitable for long-term forecasting. Moreover, its application in previous studies confirms its reliability and applicability in traffic prediction research.

Future Work

The next phase of this project involves refining the system's predictive capabilities through the use of more advanced machine learning models, such as hybrid deep learning approaches. Future work will also explore expanding the sensor network to include additional data points, such as noise pollution and energy consumption from electric vehicles. We aim to scale the system for deployment across a wider range of smart city infrastructures, with the potential for real-time integration into public transit systems and autonomous vehicle routing. A more detailed environmental impact analysis could be incorporated, taking into account longer-term effects of traffic on urban air quality.
