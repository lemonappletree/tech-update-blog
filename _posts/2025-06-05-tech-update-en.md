# 🛠️ 2025-06-05 Tech Update Summary

## 🔹 Kubernetes - Introducing Gateway API Inference Extension
The blog post introduces the Gateway API Inference Extension, which addresses traffic-routing challenges for modern generative AI and large language model (LLM) services on Kubernetes. Traditional load balancers are inadequate for these workloads, as they are often long-running, resource-intensive, and partially stateful. The Gateway API Inference Extension builds on the existing Gateway API to add inference-specific routing capabilities, transforming gateways into "Inference Gateways" and enabling a model-as-a-service approach. This extension aims to standardize routing for inference workloads, allowing for model-aware routing, request prioritization, and optimized load balancing based on real-time metrics to reduce latency and improve GPU utilization.

The extension introduces two new Custom Resources: InferencePool, which manages resource deployment and balancing, and InferenceModel, which allows AI/ML owners to manage model endpoints and traffic policies. The request flow involves extra inference-aware steps, such as Endpoint Selection, to choose the most suitable pod for a request based on live metrics. Benchmarks show that the extension provides comparable throughput to standard Kubernetes services but with significantly lower latency. The roadmap for the extension includes features like prefix-cache aware load balancing, support for large multi-modal inputs/outputs, and heterogeneous accelerators. Overall, the Gateway API Inference Extension aims to simplify and standardize AI/ML traffic routing on Kubernetes, enhancing delivery of LLM services.
👉 [Read more](https://kubernetes.io/blog/2025/06/05/introducing-gateway-api-inference-extension/)

## 🔹 Spring Boot - This Week in Spring - June 3rd, 2025
The blog post "This Week in Spring - June 3rd, 2025" provides updates and insights for Spring developers. The author shares their experience recording a session with Aleksey Stukalov, IntelliJ IDEA project lead, discussing new features for Java, Kotlin, and Spring developers. They also mention their upcoming talk at the JSpring conference. The post highlights various recent releases, including Spring Cloud 2022.0.11 and 2025.0.0, Spring Cloud Gateway versions, and Spring Modulith updates. Wim Deblauwe's release of Vite Spring Boot 0.9.0 is noted for its enhancements. Additionally, the post mentions forthcoming IntelliJ IDEA features like support for Spring Data AOT repositories and reverse engineering JPA entities, as well as upcoming Spring Modulith support.
👉 [Read more](https://spring.io/blog/2025/06/03/this-week-in-spring-june-3rd-2025)

## 🔹 Docker - Settings Management for Docker Desktop now generally available in the Admin Console
The blog post announces the general availability of Settings Management for Docker Desktop, which can now be configured through the Admin Console for Docker Business subscribers. Following a successful Early Access phase, this feature has been improved with new compliance reporting capabilities. This development fulfills Docker's vision for a centralized management solution for Docker Desktop.
👉 [Read more](https://www.docker.com/blog/settings-management-for-docker-desktop-now-generally-available-in-the-admin-console/)

## 🔹 Java - Ubuntu Ships Java, Spring, AOT
The blog post discusses a recent update on the Ubuntu Community Discourse regarding the programming toolchains available for Ubuntu application development. It highlights that Ubuntu now includes support for Java, the Spring framework, and Ahead-of-Time (AOT) compilation. The post likely provides details on how these tools are integrated into Ubuntu, their benefits for developers, and how they enhance the development process on the platform. The link provided leads to a page for further reading on the topic.
👉 [Read more](https://inside.java/2025/06/04/ubuntu-leyden/)

## 🔹 Golang - [ On | No ] syntactic support for error handling
The blog post discusses the Go programming language team's considerations regarding syntactic support for error handling. The team is evaluating whether to introduce new syntax to make error handling more concise and expressive. The post outlines different approaches being considered and highlights the importance of maintaining Go's simplicity and readability while potentially enhancing its error handling capabilities. The team seeks to balance these factors in deciding whether to implement syntactic changes.
👉 [Read more](https://go.dev/blog/error-syntax)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
The blog post announces the Helm team's participation in KubeCon + CloudNativeCon EU 2025, taking place in London from April 1 to 4. During the event, attendees can engage with Helm maintainers and learn about the development of Helm 4, which is expected to be released later in the year. The team will host talk sessions and have a presence at the Helm booth in the Project Pavilion, where participants can explore various Helm-related activities throughout the week.
👉 [Read more](https://helm.sh/blog/helm-at-kubecon-eu-25/)

