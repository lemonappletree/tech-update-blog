# 🛠️ 2025-05-04 Tech Update Summary

## 🔹 Kubernetes - Kubernetes v1.33: Mutable CSI Node Allocatable Count
The blog post discusses a new alpha feature in Kubernetes v1.33 called "mutable CSI node allocatable count." This feature allows Container Storage Interface (CSI) drivers to dynamically update the maximum number of volumes a node can handle, improving scheduling accuracy for stateful applications. Traditionally, CSI drivers reported static volume limits, but actual capacities can change, causing scheduling issues. The new feature offers periodic and reactive updates to adjust node capacities in real-time. To enable this feature, users must activate the `MutableCSINodeAllocatableCount` feature gate in `kube-apiserver` and `kubelet`, and configure their CSI drivers for periodic updates. The post encourages users to test the feature and provide feedback to help improve it.
👉 [Read more](https://kubernetes.io/blog/2025/05/02/kubernetes-1-33-mutable-csi-node-allocatable-count/)

## 🔹 Spring Boot - Spring Cloud 2025.0.0-RC1 (aka Northfields) has been released
The blog post announces the release of Spring Cloud 2025.0.0-RC1, also known as Northfields. This release is available in the Spring Milestone repository and is based on Spring Boot 3.5.0-RC1. The release includes various updates and notable changes across different Spring Cloud components:

1. **Spring Cloud Config**: Now supports YAML specific profile documents in AWS S3 buckets.
2. **Spring Cloud Gateway**: Introduces features like registering custom filters, supporting base-path in path predicates, configurable Permissions-Policy, and reloading httpClient connectTimeout configuration.
3. **Spring Cloud Task**: Includes deprecation notifications for Remote Partitioning and Task Launcher.
4. **Spring Cloud Stream**: StreamBridge no longer adds dynamic Bindings to Output/Input binding lifecycle.
5. **Spring Cloud Function**: Deprecates Spring Cloud Function Web and RSocket module, and allows the adapter to listen for additional HTTP verbs.

The post also lists the updated modules and their versions in the 2025.0.0-RC1 release and provides instructions on how to get started using the release with Maven and Gradle. Feedback is welcomed via GitHub, Gitter, Stack Overflow, and Twitter.
👉 [Read more](https://spring.io/blog/2025/05/01/spring-cloud-2025-0-0-rc1-released)

## 🔹 Docker - Update on the Docker DX extension for VS Code
The blog post discusses the release of the new Docker DX extension for Visual Studio Code, resulting from a collaboration between Docker and Microsoft. This update aims to enhance support for developers working on containerized applications. The post highlights changes and improvements made to the Docker extension in VS Code since its launch a few weeks ago. For more details, you can visit the full blog post [here](https://www.docker.com/blog/docker-dx-extension-for-vs-code-update/).
👉 [Read more](https://www.docker.com/blog/docker-dx-extension-for-vs-code-update/)

## 🔹 Java - Java for AI
The blog post titled "Java for AI" discusses how Java's existing and future features can fulfill the requirements of artificial intelligence applications. Current features like the Foreign Function and Memory API and the Vector API are highlighted for their utility in AI development. Additionally, upcoming features proposed by Project Valhalla and Project Babylon are considered for their potential impact. The post includes a video that elaborates on how these features might be utilized by Java libraries and applications to create competitive AI solutions.
👉 [Read more](https://inside.java/2025/05/03/javaone-java-ai/)

## 🔹 Golang - More predictable benchmarking with testing.B.Loop
The blog post discusses improvements in benchmarking within the Go programming language, specifically in version 1.24. It introduces the new `testing.B.Loop` feature, which aims to make benchmark results more predictable and reliable. This enhancement addresses previous challenges with benchmark looping by providing a more consistent framework for running performance tests. The article highlights how this change will benefit developers by offering more accurate performance measurements and improving the overall benchmarking process in Go.
👉 [Read more](https://go.dev/blog/testing-b-loop)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
The blog post announces that the Helm team will be attending KubeCon + CloudNativeCon EU 2025 in London from April 1-4. The team will be discussing the upcoming release of Helm 4 and encourages attendees to engage with Helm maintainers during talk sessions and at the Helm booth in the Project Pavilion. The post provides more details on Helm-related activities planned for the event.
👉 [Read more](https://helm.sh/blog/helm-at-kubecon-eu-25/)

