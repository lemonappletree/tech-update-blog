# 🛠️ 2025-05-06 Tech Update Summary

## 🔹 Kubernetes - Kubernetes v1.33: Prevent PersistentVolume Leaks When Deleting out of Order graduates to GA
The blog post announces the graduation of a feature to General Availability (GA) in Kubernetes v1.33, which prevents PersistentVolume (PV) leaks when deleting out of order. This enhancement ensures proper reclamation of storage resources, avoiding unwanted leaks. Previously, deleting a PV before its bound PersistentVolumeClaim (PVC) could result in storage assets not being removed. With Kubernetes v1.33, this issue is resolved by using finalizers, which ensure that the configured "Delete" reclaim policy is honored, even if PVs are deleted before their bound PVCs. The new behavior is implemented for CSI volumes by adding a specific finalizer to PVs. The article provides details on how the system works, notes limitations for statically provisioned in-tree plugin volumes, and explains how to enable the new behavior by upgrading to Kubernetes v1.33. It also includes references and encourages involvement in the Kubernetes Storage Special Interest Group (SIG).
👉 [Read more](https://kubernetes.io/blog/2025/05/05/kubernetes-v1-33-prevent-persistentvolume-leaks-when-deleting-out-of-order-graduate-to-ga/)

## 🔹 Spring Boot - Dynamic Tool Updates in Spring AI's Model Context Protocol
The blog post discusses the implementation of dynamic tool updates in Spring AI's Model Context Protocol (MCP). MCP is a standardized interface that allows AI models to access external tools and resources, enhancing flexibility and extensibility in AI applications. The post explains how MCP can dynamically update available tools at runtime, enabling servers to add or remove tools without restarting, and allowing clients to detect these changes and use new capabilities. This feature supports various use cases, including feature flags for AI capabilities, context-aware tool loading, progressive enhancement, and dynamic plugin architecture. The post also details the server-side and client-side implementations, emphasizing the benefits of a standardized interface, dynamic updates, automatic discovery, and a simple API. Overall, dynamic tool updates in MCP enable more adaptive and resource-efficient AI applications. For more details, the blog provides example code and links to related resources.
👉 [Read more](https://spring.io/blog/2025/05/04/spring-ai-dynamic-tool-updates-with-mcp)

## 🔹 Docker - Introducing Docker MCP Catalog and Toolkit: The Simple and Secure Way to Power AI Agents with MCP
The blog post introduces the Docker MCP Catalog and Toolkit, which aims to simplify and secure the process of connecting AI agents with external tools using Model Context Protocols (MCPs). Despite MCPs becoming the standard, the current developer experience is fragmented, with challenges in discovery, setup, and security. The post emphasizes that improving this experience requires a collaborative industry effort. Docker's new offerings provide a secure, scalable, and trusted solution to power AI agents effectively with MCPs.
👉 [Read more](https://www.docker.com/blog/announcing-docker-mcp-catalog-and-toolkit-beta/)

## 🔹 Java - Episode 35 “Stream Gatherers” with Viktor Klang
In episode 35 of the tech podcast, Ana interviews Viktor Klang, a core JDK architect and author of the Stream Gatherers JDK Enhancement Proposal. They explore the Gatherers API, a notable feature in JDK 24, discussing its development, implementation, and potential impact on Java programming.
👉 [Read more](https://inside.java/2025/05/05/podcast-035/)

## 🔹 Golang - More predictable benchmarking with testing.B.Loop
The blog post discusses improvements in benchmarking for the Go programming language, specifically with the introduction of `testing.B.Loop` in Go 1.24. This new feature aims to provide more predictable and consistent benchmarking results. By enhancing the looping mechanism used during benchmark tests, developers can obtain more reliable performance data, leading to better optimization and efficiency in Go applications.
👉 [Read more](https://go.dev/blog/testing-b-loop)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
The blog post announces that the Helm team will be attending KubeCon + CloudNativeCon EU 2025 in London from April 1 to 4. They are working on Helm 4, which is expected to be released later in the year. Attendees are encouraged to participate in discussions with Helm maintainers during talk sessions and visit the Helm booth in the Project Pavilion. The post provides more details about Helm-related activities throughout the event.
👉 [Read more](https://helm.sh/blog/helm-at-kubecon-eu-25/)

