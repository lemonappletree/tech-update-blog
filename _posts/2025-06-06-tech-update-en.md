# 🛠️ 2025-06-06 Tech Update Summary

## 🔹 Kubernetes - Introducing Gateway API Inference Extension
The blog post introduces the Gateway API Inference Extension, designed to tackle the unique traffic-routing challenges posed by generative AI and large language model (LLM) services on Kubernetes. Traditional load balancers are insufficient for these workloads, which require specialized capabilities due to their long-running, resource-intensive, and partially stateful nature. The Inference Extension builds on the existing Gateway API, adding inference-specific routing capabilities to create an Inference Gateway. This approach enables standardized and efficient routing for AI/ML workloads, optimizing model-aware routing, supporting request criticalities, and improving load balancing. The extension introduces two Custom Resources (CRDs): InferencePool, for managing resource usage and deployment, and InferenceModel, for user-facing model endpoints. The request flow incorporates inference-aware steps for smarter routing, which reduces latency and optimizes GPU utilization. Benchmarks show the extension delivers comparable throughput with significantly lower latency compared to standard Kubernetes Services. The roadmap includes features like prefix-cache aware load balancing, support for heterogeneous accelerators, and expanded model types. Overall, the extension aims to simplify and standardize AI/ML traffic routing, aligning with Kubernetes-native tooling.
👉 [Read more](https://kubernetes.io/blog/2025/06/05/introducing-gateway-api-inference-extension/)

## 🔹 Spring Boot - A Bootiful Podcast: IntelliJ IDEA lead Aleksey Stukalov
The blog post is about a podcast episode where the host talks with Aleksey Stukalov, the lead of IntelliJ IDEA. The conversation likely covers topics related to IntelliJ IDEA, its features, and insights from Aleksey's experience leading the project.
👉 [Read more](https://spring.io/blog/2025/06/05/a-bootiful-podcast-aleksey-stukalov)

## 🔹 Docker - Settings Management for Docker Desktop now generally available in the Admin Console
The blog post announces that Settings Management for Docker Desktop is now generally available through the Admin Console for Docker Business subscribers. After a successful Early Access phase, this feature has been improved with new compliance reporting capabilities, fulfilling the aim for a centralized management solution for Docker Desktop.
👉 [Read more](https://www.docker.com/blog/settings-management-for-docker-desktop-now-generally-available-in-the-admin-console/)

## 🔹 Java - Java 25 Brings 18 JEPs 😱 Inside Java Newscast #92
The tech blog post discusses the upcoming release of Java 25, scheduled for September 16th. The release will include 18 Java Enhancement Proposals (JEPs), with 11 finalized features that enhance the language, APIs, and runtime, and an additional 7 features still in development. The blog suggests that the next long-term support release will be significant and recommends a prompt update to take advantage of the new improvements.
👉 [Read more](https://inside.java/2025/06/05/newscast-92/)

## 🔹 Golang - [ On | No ] syntactic support for error handling
The blog post discusses the Go programming language team's considerations regarding syntactic support for error handling. They are evaluating the potential inclusion of new syntax to improve error handling in Go, weighing the benefits and drawbacks of such changes. The post outlines the team's current plans and thought process, aiming to enhance the language's usability while maintaining its simplicity and efficiency.
👉 [Read more](https://go.dev/blog/error-syntax)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
The blog post announces that the Helm team will be attending KubeCon + CloudNativeCon EU 2025 in London, UK, from April 1-4. They are preparing for the release of Helm 4 later this year and encourage attendees to engage with their maintainers during talk sessions and at the Helm booth in the Project Pavilion. The post provides more details about Helm-related activities happening throughout the week.
👉 [Read more](https://helm.sh/blog/helm-at-kubecon-eu-25/)

