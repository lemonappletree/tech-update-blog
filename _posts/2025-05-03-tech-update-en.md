# 🛠️ 2025-05-03 Tech Update Summary

## 🔹 Kubernetes - Kubernetes v1.33: Mutable CSI Node Allocatable Count
The blog post discusses a new alpha feature in Kubernetes v1.33 called "mutable CSI node allocatable count," which enhances the scheduling of stateful applications by allowing Container Storage Interface (CSI) drivers to dynamically update the maximum number of volumes a node can handle. Traditionally, CSI drivers report static volume limits, which can lead to scheduling issues when actual capacities change. The new feature allows for more accurate pod scheduling by supporting periodic and reactive updates to node capacity information. To enable this feature, the `MutableCSINodeAllocatableCount` feature gate must be activated in the `kube-apiserver` and `kubelet` components, and CSI drivers configured accordingly. This feature aims to reduce scheduling failures and improve cluster health by ensuring up-to-date resource availability information. Users are encouraged to test the feature and provide feedback to help guide its development.
👉 [Read more](https://kubernetes.io/blog/2025/05/02/kubernetes-1-33-mutable-csi-node-allocatable-count/)

## 🔹 Spring Boot - A Bootiful Podcast: Spring instructor Mary Ellen Bowman
In the podcast episode titled "A Bootiful Podcast: Spring instructor Mary Ellen Bowman," the host engages in a conversation with Mary Ellen Bowman, who is renowned for her expertise as a Spring instructor. The discussion likely explores her experiences, insights, and contributions to the Spring community.
👉 [Read more](https://spring.io/blog/2025/05/01/a-bootiful-podcast-mary-ellen-bowman)

## 🔹 Docker - Update on the Docker DX extension for VS Code
The blog post discusses the recent release of the Docker DX extension for Visual Studio Code, highlighting the collaboration between Docker and Microsoft to enhance support for developers creating containerized applications. Since its launch, users may have observed updates to their Docker extension in VS Code. The post likely details the improvements and new features introduced with this extension, aimed at improving the developer experience.
👉 [Read more](https://www.docker.com/blog/docker-dx-extension-for-vs-code-update/)

## 🔹 Java - JEP targeted to JDK 25: 511: Module Import Declarations
The blog post discusses JEP 511, which is targeted for JDK 25 and focuses on the introduction of module import declarations. This enhancement aims to improve the Java module system by allowing developers to import modules more explicitly and manage dependencies more effectively. The post likely provides details on how this change will impact Java development, the benefits it brings, and any potential challenges it addresses. More information can be found in the linked article.
👉 [Read more](https://inside.java/2025/05/02/jep511-target-jdk25/)

## 🔹 Golang - More predictable benchmarking with testing.B.Loop
The blog post discusses improvements in benchmark looping introduced in Go version 1.24, specifically focusing on the `testing.B.Loop` feature. This enhancement aims to provide more predictable and consistent benchmarking results. By refining how benchmark loops are handled, developers can achieve more reliable performance metrics, ultimately aiding in the optimization and evaluation of Go code. The post highlights the benefits of this update and how it contributes to more accurate benchmarking practices in Go.
👉 [Read more](https://go.dev/blog/testing-b-loop)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
The Helm team is attending KubeCon + CloudNativeCon EU 2025 in London, UK, from April 1-4. They are preparing for the release of Helm 4 later in the year. Attendees are encouraged to engage with Helm maintainers during talk sessions and visit the Helm booth in the Project Pavilion. The blog post provides additional details on all Helm-related activities happening throughout the week.
👉 [Read more](https://helm.sh/blog/helm-at-kubecon-eu-25/)

