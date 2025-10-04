# 🛠️ 2025-10-04 Tech Update Summary

## 🔹 Kubernetes - Announcing Changed Block Tracking API support (alpha)
The blog post announces the alpha support for a Changed Block Tracking (CBT) API in Kubernetes. This feature allows CSI storage drivers to efficiently identify changed blocks in PersistentVolume snapshots, enhancing backup operations by focusing only on modified data. The API, currently applicable only to block volumes, is aimed at improving backup efficiency by reducing time, resource usage, and storage costs. Key components of the implementation include the CSI SnapshotMetadata Service API, a Kubernetes CustomResourceDefinition (CRD), and an external snapshot metadata sidecar. Storage providers must implement specific RPCs and ensure backend capabilities for block-level change tracking, while backup solutions need to handle authentication and develop streaming client-side code. The feature is expected to move to beta in future releases based on feedback and adoption. The blog encourages community involvement and provides resources for getting started with the feature.
👉 [Read more](https://kubernetes.io/blog/2025/09/25/csi-changed-block-tracking/)

## 🔹 Spring Boot - Spring Cloud 2025.1.0-M3 (aka Oakwood) has been released
The tech blog post announces the release of Spring Cloud 2025.1.0-M3, also known as Oakwood. This milestone release is now available in the Spring Milestone repository. It includes significant updates and changes across various components, such as Spring Cloud Function, which has discontinued certain modules; Spring Cloud Kubernetes, with upgrades to Kubernetes Java Client and Fabric8 Kubernetes Client; and Spring Cloud Contract, which has undergone a property migration. Additionally, Spring Cloud Circuitbreaker has upgraded to Resilience4j 2.3.0, and Spring Cloud Commons has added LoadBalancer API versioning support. Several modules have been updated to version 5.0.0-M3, including Spring Cloud Stream, Config, Build, Kubernetes, and others. The release is compatible with Spring Boot 4.0.0-M3. The blog post provides links to the release notes, GitHub issues, and instructions for getting started with Maven and Gradle. Feedback is encouraged via various platforms such as GitHub, Gitter, Stack Overflow, and Twitter.
👉 [Read more](https://spring.io/blog/2025/10/03/spring-cloud-2025-1-0-M3-aka-oakwood-has-been-released)

## 🔹 Docker - From Shell Scripts to Science Agents: How AI Agents Are Transforming Research Workflows
The tech blog post titled "From Shell Scripts to Science Agents: How AI Agents Are Transforming Research Workflows" discusses the challenges researchers face when managing complex scientific tasks, such as running models, analyzing data, and reviewing literature. The post illustrates a typical scenario where a researcher is working late at night with multiple screens and tools open to handle different aspects of their workflow. The article highlights how AI agents are revolutionizing these research workflows by automating and streamlining tasks, which allows scientists to focus more on their core research activities. AI agents can handle tasks like data parsing, literature searches, and model execution, making the research process more efficient and less prone to human error.
👉 [Read more](https://www.docker.com/blog/ai-science-agents-research-workflows/)

## 🔹 Java - The Inside Java Newsletter: Java 25 is Live!
The Inside Java Newsletter for September 2025 highlights the release of Java 25, featuring a series of technical videos about the new version. It provides updates on Java User Groups, developer events, learning resources, community podcasts, and content from the Java Platform Group. Readers are encouraged to visit learn.java, dev.java, and inside.java for a variety of multimedia content suitable for developers, learners, educators, and customers. The newsletter also offers options to view archives, subscribe, and share with friends.
👉 [Read more](https://inside.java/2025/10/03/inside-java-newsletter/)

## 🔹 Golang - Flight Recorder in Go 1.25
The blog post discusses the introduction of a new feature called "flight recording" in Go 1.25. This tool is designed to enhance diagnostics by capturing detailed information about a program's execution. It allows developers to trace and analyze program behavior, providing valuable insights for debugging and performance optimization. The feature aims to improve the overall development experience by making it easier to identify and address issues in Go applications.
👉 [Read more](https://go.dev/blog/flight-recorder)

## 🔹 Helm - Path To Releasing Helm v4
The blog post discusses the release of the first Alpha version of Helm v4, marking a significant step towards the final release. It outlines the current development status and provides insights into the upcoming features and changes in Helm v4. The post also encourages the community to participate in the development process, offering ways to contribute and engage with the project.
👉 [Read more](https://helm.sh/blog/path-to-helm-v4/)

