# 🛠️ 2025-05-11 Tech Update Summary

## 🔹 Kubernetes - Kubernetes v1.33: Streaming List responses
The blog post discusses a new feature in Kubernetes v1.33, which introduces streaming encoding for List responses to help manage cluster stability as infrastructure scales. Previously, handling large List requests could lead to high memory consumption, potentially causing Out-of-Memory (OOM) issues. The new streaming encoder addresses this by processing each item in a List individually rather than as a single large block, allowing for incremental memory release and reducing the API server's memory footprint. This results in improved scalability, reduced memory usage, increased stability, and better resource utilization. The blog also highlights performance gains, noting a 20x reduction in memory usage during benchmarks. The change is backward compatible and requires no client-side modifications.
👉 [Read more](https://kubernetes.io/blog/2025/05/09/kubernetes-v1-33-streaming-list-responses/)

## 🔹 Spring Boot - A Bootiful Podcast: V Körbes on security from the platform on up
In this tech blog post titled "A Bootiful Podcast: V Körbes on security from the platform on up," the author discusses a podcast episode featuring an interview with V Körbes from Broadcom. The conversation centers around Körbes' work on security, focusing on both the application level and the underlying platform. The post targets fans of Spring, a popular Java framework, and highlights the importance of holistic security measures in software development.
👉 [Read more](https://spring.io/blog/2025/05/08/a-bootiful-podcast-v-korbes)

## 🔹 Docker - Securing Model Context Protocol: Safer Agentic AI with Containers
The blog post discusses the growing adoption of Model Context Protocol (MCP) tools, which are used to increase the autonomy of AI agents. As these tools become more widely used, security concerns have become more pressing. The post highlights risks such as misalignment between the behavior of AI agents and user expectations, as well as the potential for uncontrolled execution. The blog emphasizes the need for improved security measures to address these challenges as the adoption of MCP tools continues to accelerate.
👉 [Read more](https://www.docker.com/blog/whats-next-for-mcp-security/)

## 🔹 Java - JavaFX 24 and Beyond
The blog post titled "JavaFX 24 and Beyond" discusses the latest advancements in the JavaFX graphical UI toolkit, which is used for building desktop and mobile applications. The post highlights new features introduced with the release of JavaFX 24, including the RichTextArea (incubator), CSS Transitions, and Platform Preferences. The session promises numerous demos and sample code to illustrate these features. Additionally, the post offers a sneak peek into future developments for JavaFX.
👉 [Read more](https://inside.java/2025/05/10/javaone-javafx/)

## 🔹 Golang - More predictable benchmarking with testing.B.Loop
The blog post discusses the introduction of the `testing.B.Loop` feature in Go 1.24, aimed at improving the predictability of benchmark tests. This new feature allows developers to write more reliable and consistent benchmarks by providing a better structure for looping in benchmark functions. The post explains how `testing.B.Loop` enhances the accuracy of performance measurements, making it easier for developers to identify performance regressions and optimizations in their Go code.
👉 [Read more](https://go.dev/blog/testing-b-loop)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
The blog post announces that the Helm team will be attending KubeCon + CloudNativeCon EU 2025 in London from April 1 to 4. With Helm 4 set to release later in the year, the team encourages attendees to engage with Helm maintainers during talk sessions and visit the Helm booth in the Project Pavilion for more Helm-related activities throughout the week.
👉 [Read more](https://helm.sh/blog/helm-at-kubecon-eu-25/)

