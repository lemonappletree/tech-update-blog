# 🛠️ 2025-05-17 Tech Update Summary

## 🔹 Kubernetes - Kubernetes v1.33: In-Place Pod Resize Graduated to Beta
The blog post announces that the "in-place Pod resize" feature in Kubernetes, which allows for changing CPU and memory resources of a running Pod without restarting it, has graduated to Beta in version 1.33. This feature, initially introduced as alpha in v1.27, reduces disruption for stateful applications and improves resource utilization and scaling speed. The update includes user-facing changes like the new `resize` subresource to modify Pod resources, status updates via conditions, and support for resizing sidecar containers. There have been improvements in stability, reliability, and integration with container runtimes. Future developments will focus on stability, addressing current limitations, integrating with the VerticalPodAutoscaler (VPA), and gathering user feedback. Users are encouraged to experiment with the feature, which is enabled by default in v1.33, and provide feedback through Kubernetes channels.
👉 [Read more](https://kubernetes.io/blog/2025/05/16/kubernetes-v1-33-in-place-pod-resize-beta/)

## 🔹 Spring Boot - Spring Data 2025.0.0 goes GA
The blog post announces the general availability of Spring Data 2025.0.0, which is now accessible via Maven Central. This release includes driver updates and enhancements across different store modules. Key changes include support for vector types and vector search in MongoDB and Apache Cassandra, constructor expression derivation for DTO projections in Spring Data JPA, identifier generation using sequences in Spring Data JDBC and R2DBC, and index creation using Cassandra 5 Storage-Attached Indexes. The post also notes that Spring Boot 3.5 will upgrade to Spring Data 2025.0.0, which is the final feature release of the 3.x development line. Future development will focus on the 4.0 release, with an expected general availability in November 2025. The blog provides links to documentation, Javadoc, and changelogs for various Spring Data modules.
👉 [Read more](https://spring.io/blog/2025/05/16/spring-data-2025-0-goes-ga)

## 🔹 Docker - Docker at Microsoft Build 2025: Where Secure Software Meets Intelligent Innovation
The blog post discusses Docker's participation at Microsoft Build 2025, highlighting how the company is integrating developer experience, security, and AI innovation into its latest products. Attendees, both in-person in Seattle and online, will learn about Docker's new tools and solutions that are transforming the development, security, and scaling of modern applications. The post emphasizes Docker's vision for developers and its commitment to enhancing the way teams create software.
👉 [Read more](https://www.docker.com/blog/docker-at-microsoft-build-2025/)

## 🔹 Java - Mastering JVM Memory Troubleshooting - From OutOfMemoryErrors to Leaks
The blog post titled "Mastering JVM Memory Troubleshooting - From OutOfMemoryErrors to Leaks" discusses the complexities of diagnosing memory issues in Java applications. It highlights that these problems often present subtle symptoms, making them challenging to identify. The post delves into various common and less obvious memory issues, such as Java heap exhaustion, metaspace overflows, and native memory leaks, providing insights on how to troubleshoot these issues effectively.
👉 [Read more](https://inside.java/2025/05/15/javaone-jvm-troubleshooting/)

## 🔹 Golang - More predictable benchmarking with testing.B.Loop
The blog post discusses improvements in benchmark looping introduced in Go 1.24 through the `testing.B.Loop` function. This enhancement aims to provide more predictable and reliable benchmarking results by refining how benchmarks are executed and measured. The new approach helps developers obtain more consistent performance metrics, making it easier to evaluate and optimize their Go code.
👉 [Read more](https://go.dev/blog/testing-b-loop)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
The blog post announces that the Helm team will be attending KubeCon + CloudNativeCon EU 2025 in London from April 1 to 4. They are working on Helm 4, which is set to be released later in the year. Attendees are encouraged to join discussions with Helm maintainers during talk sessions and visit the Helm booth in the Project Pavilion for more information on Helm-related activities throughout the week.
👉 [Read more](https://helm.sh/blog/helm-at-kubecon-eu-25/)

