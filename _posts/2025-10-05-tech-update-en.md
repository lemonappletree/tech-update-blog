# 🛠️ 2025-10-05 Tech Update Summary

## 🔹 Kubernetes - Announcing Changed Block Tracking API support (alpha)
The blog post announces the alpha release of a new Changed Block Tracking API for Kubernetes, enhancing storage efficiency by allowing CSI storage drivers to identify changes at the block level within PersistentVolume snapshots. This feature aims to streamline backup operations by focusing only on changed data, leading to faster and more resource-efficient processes. The API currently supports only block volumes, excluding file volumes. Key benefits include reduced backup windows, lower resource utilization, and decreased storage costs. The implementation involves multiple components, including the CSI SnapshotMetadata Service API, and requires specific responsibilities from storage providers and backup solutions. The post encourages users to try out the feature and provides links to relevant documentation and resources for further exploration and involvement with the Kubernetes Storage Special Interest Group.
👉 [Read more](https://kubernetes.io/blog/2025/09/25/csi-changed-block-tracking/)

## 🔹 Spring Boot - Spring Cloud 2025.1.0-M3 (aka Oakwood) has been released
The blog post announces the release of Spring Cloud 2025.1.0-M3, also known as Oakwood. This milestone release is now available in the Spring Milestone repository. Notable changes include dependencies on Spring Boot 4.0.0-M3 and updates across various Spring Cloud modules. Key changes involve discontinuing certain Spring Cloud Function components, upgrading Kubernetes Java and Fabric8 clients, and migrating Spring Cloud Contract properties. The release also upgrades Resilience4j and adds LoadBalancer API versioning support in Spring Cloud Commons. Updated modules include Spring Cloud Stream, Config, Build, Kubernetes, Task, Contract, Consul, Gateway, Netflix, Circuitbreaker, Vault, Function, Bus, Zookeeper, Commons, Starter Build, and Openfeign, all to version 5.0.0-M3. Feedback is encouraged via GitHub, Gitter, Stack Overflow, and Twitter. The post provides instructions for integrating this release with Maven and Gradle.
👉 [Read more](https://spring.io/blog/2025/10/03/spring-cloud-2025-1-0-M3-aka-oakwood-has-been-released)

## 🔹 Docker - From Shell Scripts to Science Agents: How AI Agents Are Transforming Research Workflows
The blog post titled "From Shell Scripts to Science Agents: How AI Agents Are Transforming Research Workflows" discusses the integration of AI agents into research processes. It paints a picture of a typical late-night scenario in a lab where a researcher is managing multiple tasks, such as running protein folding models, parsing CSV files, and searching for literature, all while using various tools like Jupyter notebooks and Excel. The article emphasizes how AI agents can streamline these workflows by automating repetitive tasks, improving data management, and enhancing research efficiency, ultimately transforming the way scientific research is conducted.
👉 [Read more](https://www.docker.com/blog/ai-science-agents-research-workflows/)

## 🔹 Java - The Inside Java Newsletter: Java 25 is Live!
The blog post discusses the September 2025 edition of the Inside Java Newsletter, which highlights the release of Java 25. It features a series of technical videos about the new version and provides updates on Java User Groups, developer events, learning resources, community podcasts, and content from the Java Platform Group. The post encourages readers to visit learn.java, dev.java, and inside.java for a variety of multimedia content aimed at developers, learners, educators, and customers. It also invites readers to explore the newsletter archives, subscribe, and share the newsletter with friends.
👉 [Read more](https://inside.java/2025/10/03/inside-java-newsletter/)

## 🔹 Golang - Flight Recorder in Go 1.25
The blog post discusses the introduction of a new diagnostic tool called "flight recording" in Go version 1.25. This feature aims to enhance the ability to monitor, record, and diagnose the behavior of Go programs. Flight recording provides a more detailed and continuous stream of diagnostic information, allowing developers to better understand the execution and performance of their applications. This addition is expected to be a valuable resource for troubleshooting and optimizing Go programs.
👉 [Read more](https://go.dev/blog/flight-recorder)

## 🔹 Helm - Path To Releasing Helm v4
The blog post announces the release of the first Alpha version for Helm v4, marking a significant milestone in its development. It provides details about the current progress of Helm v4 and encourages the broader community to participate in its development process. The post aims to keep the community informed and engaged as Helm v4 approaches its final stages of development. For more information, readers are directed to visit the provided link.
👉 [Read more](https://helm.sh/blog/path-to-helm-v4/)

