# 🛠️ 2025-05-13 Tech Update Summary

## 🔹 Kubernetes - Kubernetes v1.33: Image Pull Policy the way you always thought it worked!
The blog post discusses a significant update in Kubernetes v1.33 regarding the `imagePullPolicy`. Previously, the `IfNotPresent` policy allowed pods to use already pulled private images without verifying credentials, leading to potential security issues. In v1.33, Kubernetes addresses this by ensuring that the Kubelet verifies a pod's credentials before allowing it to use a locally cached image. This change enhances security by ensuring that only authorized pods can access private images. The update also includes improvements for performance and service stability, such as reduced need for re-authentication when using the same credentials. The post details the workings of the new feature, encourages users to try the alpha version, and outlines future plans for further enhancements. It invites interested individuals to get involved through Kubernetes community channels.
👉 [Read more](https://kubernetes.io/blog/2025/05/12/kubernetes-v1-33-ensure-secret-pulled-images-alpha/)

## 🔹 Spring Boot - A Bootiful Podcast: V Körbes on security from the platform on up
In this blog post, the author discusses a special episode of "A Bootiful Podcast" where they have a conversation with V Körbes from Broadcom. The discussion focuses on security practices and considerations at various levels, both above and below the application layer. This episode provides insights into how security can be integrated throughout different layers of the technology stack.
👉 [Read more](https://spring.io/blog/2025/05/08/a-bootiful-podcast-v-korbes)

## 🔹 Docker - Securing Model Context Protocol: Safer Agentic AI with Containers
The tech blog post titled "Securing Model Context Protocol: Safer Agentic AI with Containers" discusses the emerging security concerns associated with the broader adoption of Model Context Protocol (MCP) tools. While these tools are primarily used by early adopters, their usage is rapidly expanding. The post highlights the risks introduced by increased agent autonomy, such as potential misalignment between agent behavior and user expectations, as well as issues with uncontrolled execution. The article suggests that using containers can help address these security challenges, ensuring safer deployment and management of agentic AI systems.
👉 [Read more](https://www.docker.com/blog/whats-next-for-mcp-security/)

## 🔹 Java - JEP targeted to JDK 25: 505: Structured Concurrency (5th Preview)
The blog post discusses JEP 505, which is targeted for JDK 25 and focuses on Structured Concurrency in its fifth preview. Structured Concurrency aims to simplify multithreaded programming by treating multiple tasks running in different threads as a single unit of work. This approach enhances error handling and cancellation, making concurrent programming more predictable and reliable. The JEP's inclusion in JDK 25 indicates ongoing improvements and refinements in Java's concurrency model to make it easier for developers to write efficient and error-free concurrent programs.
👉 [Read more](https://inside.java/2025/05/12/jep505-target-jdk25/)

## 🔹 Golang - More predictable benchmarking with testing.B.Loop
The blog post discusses improvements in benchmarking for the Go programming language with the introduction of `testing.B.Loop` in Go version 1.24. This new feature aims to provide more predictable and consistent benchmarking results. It enhances the process of benchmarking loops, making it easier for developers to measure performance with greater accuracy. The post highlights how `testing.B.Loop` can lead to better performance analysis and optimization in Go applications.
👉 [Read more](https://go.dev/blog/testing-b-loop)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
The blog post announces the Helm team's participation in KubeCon + CloudNativeCon EU 2025, taking place in London from April 1 to 4. The team is preparing for the release of Helm 4 later in the year and invites attendees to engage with Helm maintainers during talk sessions and visit their booth in the Project Pavilion. The post provides more details about Helm-related activities scheduled for the event.
👉 [Read more](https://helm.sh/blog/helm-at-kubecon-eu-25/)

