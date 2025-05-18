# 🛠️ 2025-05-18 Tech Update Summary

## 🔹 Kubernetes - Kubernetes v1.33: In-Place Pod Resize Graduated to Beta
The blog post announces that the in-place Pod resize feature, also known as In-Place Pod Vertical Scaling, has progressed to Beta status and is enabled by default in Kubernetes v1.33. This feature allows CPU and memory resources of running Pods to be adjusted without requiring a restart, reducing disruption for stateful applications and improving resource utilization. Notable updates from its alpha version include the introduction of a "resize" subresource for modifying resources, status conditions indicating resize progress, and support for sidecar containers. Enhancements in stability, reliability, and faster resize detection have been made, along with numerous bug fixes. The community is focusing on further improving the feature, addressing limitations, integrating with VerticalPodAutoscaler, and gathering user feedback. The post encourages users to experiment with the feature and provide feedback through official Kubernetes channels.
👉 [Read more](https://kubernetes.io/blog/2025/05/16/kubernetes-v1-33-in-place-pod-resize-beta/)

## 🔹 Spring Boot - Spring Data 2025.0.0 goes GA
The blog post announces the general availability of Spring Data 2025.0.0, which is now accessible from Maven Central. This release includes upgrades to drivers and enhancements in specific store modules. Key updates feature support for vector types and vector search in MongoDB and Apache Cassandra, constructor expression derivation for DTO projections in Spring Data JPA, identifier generation using sequences in Spring Data JDBC and R2DBC, and index creation using Cassandra 5 Storage-Attached Indexes.

Additionally, Spring Boot 3.5 will update to use Spring Data 2025.0.0. This release is the last feature release in the 3.x development line, with the 4.0 release scheduled for November 2025. The post includes links to detailed release notes, documentation, and changelogs for various Spring Data modules.
👉 [Read more](https://spring.io/blog/2025/05/16/spring-data-2025-0-goes-ga)

## 🔹 Docker - Docker at Microsoft Build 2025: Where Secure Software Meets Intelligent Innovation
At Microsoft Build 2025, Docker is set to showcase a blend of enhanced developer experiences, robust security measures, and cutting-edge AI innovations through their latest product announcements. The event, accessible both in-person at the Seattle Convention Center and online, will highlight how Docker is transforming the development, security, and scaling of modern applications. The focus is on redefining the developer experience by integrating intelligent solutions that streamline application development and deployment processes. Docker's presence at the event emphasizes their commitment to empowering development teams with tools that enhance productivity and security in the evolving tech landscape.
👉 [Read more](https://www.docker.com/blog/docker-at-microsoft-build-2025/)

## 🔹 Java - Java 24, Faster Than Ever
The blog post titled "Java 24, Faster Than Ever" discusses the continuous performance enhancements in Java, which enable existing applications to run more efficiently with each new release of Java. The post explores five recent performance improvements in the Java Development Kit (JDK), focusing on enhancements in standard Java libraries, the Just-In-Time (JIT) compiler, and garbage collectors. These improvements contribute to the overall speed and efficiency of Java applications without requiring changes to the application code.
👉 [Read more](https://inside.java/2025/05/17/javaone-faster-jdk24/)

## 🔹 Golang - More predictable benchmarking with testing.B.Loop
The blog post discusses improvements in benchmark looping with the introduction of `testing.B.Loop` in Go 1.24. This enhancement aims to make benchmarking more predictable and reliable by providing a more consistent way to manage loop iterations during performance testing. The post highlights how `testing.B.Loop` offers better control over iteration counts, leading to more accurate and stable benchmark results. This change is particularly beneficial for developers looking to optimize their code by providing clearer insights into its performance.
👉 [Read more](https://go.dev/blog/testing-b-loop)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
The blog post announces that the Helm team will be attending KubeCon + CloudNativeCon EU 2025 in London from April 1 to 4. They will be discussing the upcoming release of Helm 4, which is expected later in the year. Attendees are encouraged to join the Helm team for discussions during their talk sessions and visit their booth in the Project Pavilion. The post promises further details on all Helm-related activities throughout the event.
👉 [Read more](https://helm.sh/blog/helm-at-kubecon-eu-25/)

