# 🛠️ 2025-05-19 Tech Update Summary

## 🔹 Kubernetes - Kubernetes v1.33: In-Place Pod Resize Graduated to Beta
The tech blog post announces that the "in-place Pod resize" feature, also known as In-Place Pod Vertical Scaling, has graduated to Beta and will be enabled by default in Kubernetes v1.33. This feature allows for changing CPU and memory resources of running Pods without needing a restart, which is beneficial for stateful applications, batch jobs, and workloads sensitive to restarts. The post highlights the benefits of the feature, such as reduced disruption, improved resource utilization, and faster scaling. It also details changes made since the alpha version, including introducing a "resize" subresource, enhanced status reporting, sidecar support, and various stability and reliability improvements. The community's next focus is on further stabilizing the feature, addressing limitations, integrating with VerticalPodAutoscaler, and gathering user feedback. The post encourages users to experiment with the feature and provide feedback to help prioritize future enhancements.
👉 [Read more](https://kubernetes.io/blog/2025/05/16/kubernetes-v1-33-in-place-pod-resize-beta/)

## 🔹 Spring Boot - Spring Data 2025.0.0 goes GA
The blog post announces the general availability of Spring Data 2025.0.0 from Maven Central, highlighting driver upgrades and refinements in individual store modules. Key updates include vector type and vector search support in MongoDB and Apache Cassandra, constructor expression derivation for DTO projections in Spring Data JPA, identifier generation using sequences in Spring Data JDBC and R2DBC, and index creation using Cassandra 5 storage-attached indexes. The release will be integrated with Spring Boot 3.5, marking the last feature release of the 3.x development line as the team prepares for the 4.0 release expected in November 2025. The post provides links to documentation and changelogs for various modules like Spring Data JPA, MongoDB, Neo4j, and others.
👉 [Read more](https://spring.io/blog/2025/05/16/spring-data-2025-0-goes-ga)

## 🔹 Docker - Docker at Microsoft Build 2025: Where Secure Software Meets Intelligent Innovation
The blog post discusses Docker's participation at Microsoft Build 2025, focusing on enhancing developer experience by integrating security and AI innovation. Docker plans to unveil new products that redefine how teams build, secure, and scale modern applications. The event, taking place at the Seattle Convention Center and online, highlights Docker's vision for developers and its commitment to advancing software development practices.
👉 [Read more](https://www.docker.com/blog/docker-at-microsoft-build-2025/)

## 🔹 Java - Java 24, Faster Than Ever
The blog post titled "Java 24, Faster Than Ever" discusses the ongoing evolution of Java's performance, highlighting how applications can run increasingly faster with each new Java release without needing changes in the application code. The post delves into five specific performance improvements in the JDK, focusing on enhancements in the standard Java libraries, the Just-In-Time (JIT) compiler, and garbage collectors.
👉 [Read more](https://inside.java/2025/05/17/javaone-faster-jdk24/)

## 🔹 Golang - More predictable benchmarking with testing.B.Loop
The blog post discusses improvements to benchmark looping in Go 1.24, focusing on the `testing.B.Loop` feature. This enhancement aims to make benchmarking more predictable by providing a more consistent and efficient way to measure performance in Go programs. The post likely explains how `testing.B.Loop` works, its benefits over previous methods, and its impact on writing and running benchmarks. Overall, the update is designed to help developers obtain more reliable benchmarking results in their Go applications.
👉 [Read more](https://go.dev/blog/testing-b-loop)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
The blog post announces the Helm team's participation in KubeCon + CloudNativeCon EU 2025, which will take place in London from April 1 to 4. The team will discuss the upcoming release of Helm 4 and invites attendees to join conversations with maintainers during talk sessions and visit the Helm booth in the Project Pavilion. The post provides details on all Helm-related activities scheduled throughout the week.
👉 [Read more](https://helm.sh/blog/helm-at-kubecon-eu-25/)

