# 🛠️ 2025-05-05 Tech Update Summary

## 🔹 Kubernetes - Kubernetes v1.33: Mutable CSI Node Allocatable Count
The blog post discusses a new alpha feature in Kubernetes v1.33 called "mutable CSI node allocatable count." This feature allows Container Storage Interface (CSI) drivers to dynamically update the maximum number of volumes a node can handle, improving the accuracy of pod scheduling and reducing errors caused by outdated volume capacity information. Traditionally, CSI drivers reported a static volume limit, which could lead to scheduling failures when actual capacities changed. The new feature enables periodic and reactive updates to node capacities, ensuring the scheduler has the most accurate data. To enable this feature, users must activate the `MutableCSINodeAllocatableCount` feature gate on the `kube-apiserver` and `kubelet` components and configure their CSI drivers accordingly. This feature is currently in alpha, and the Kubernetes community is seeking feedback to help develop it further.
👉 [Read more](https://kubernetes.io/blog/2025/05/02/kubernetes-1-33-mutable-csi-node-allocatable-count/)

## 🔹 Spring Boot - Dynamic Tool Updates in Spring AI's Model Context Protocol
The blog post discusses the Model Context Protocol (MCP) in Spring AI, a feature that allows AI models to access external tools and resources via a standardized interface. A key capability of MCP is its support for dynamic tool updates, enabling tools to be added or removed at runtime without restarting applications. The post details how Spring AI implements this feature, providing flexibility and extensibility for AI-powered applications. It covers both server-side and client-side implementations, illustrating how servers can dynamically manage tools and clients can respond to these changes. Practical applications include feature flags for AI capabilities, context-aware tool loading, and dynamic plugin architecture. The blog emphasizes MCP's standardized interface, dynamic updates, automatic discovery, and simple API as major benefits for developers creating adaptable AI applications. Additional resources and example code are provided for further exploration.
👉 [Read more](https://spring.io/blog/2025/05/04/spring-ai-dynamic-tool-updates-with-mcp)

## 🔹 Docker - Update on the Docker DX extension for VS Code
The blog post discusses the recent release of the new Docker DX extension for Visual Studio Code, marking an enhanced partnership between Docker and Microsoft. This collaboration aims to provide better support for developers working on containerized applications. Since the launch, users may have observed some updates to their Docker extension in VS Code, as this new extension is rolled out. For further details, readers are directed to the full post on Docker's blog.
👉 [Read more](https://www.docker.com/blog/docker-dx-extension-for-vs-code-update/)

## 🔹 Java - Java for AI
The blog post titled "Java for AI" highlights how Java's current and upcoming features are well-suited for AI development. Existing features like the Foreign Function and Memory API and the Vector API are already beneficial. Future enhancements, envisioned by Project Valhalla and Project Babylon, are also promising for AI solutions. The post includes a video discussing these features and their potential applications in Java libraries and applications to create competitive AI solutions.
👉 [Read more](https://inside.java/2025/05/03/javaone-java-ai/)

## 🔹 Golang - More predictable benchmarking with testing.B.Loop
The blog post discusses the introduction of `testing.B.Loop` in Go 1.24, aimed at improving the consistency and predictability of benchmark tests. This new feature modifies how benchmarks are executed, providing a more structured and reliable approach to looping. By utilizing `testing.B.Loop`, developers can achieve more stable and repeatable results in their benchmark tests, leading to more accurate performance assessments. This enhancement is part of Go's ongoing efforts to improve its testing framework's efficiency and usability.
👉 [Read more](https://go.dev/blog/testing-b-loop)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
The blog post announces that the Helm team will be attending KubeCon + CloudNativeCon EU 2025 in London, UK, from April 1-4. They are working on Helm 4, set to release later in the year, and invite attendees to engage with their maintainers during talk sessions and visit their booth in the Project Pavilion. The post includes details about Helm-related activities throughout the week.
👉 [Read more](https://helm.sh/blog/helm-at-kubecon-eu-25/)

