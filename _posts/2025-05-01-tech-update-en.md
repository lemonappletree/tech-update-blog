# 🛠️ 2025-05-01 Tech Update Summary

## 🔹 Kubernetes - Kubernetes v1.33: Storage Capacity Scoring of Nodes for Dynamic Provisioning (alpha)
The blog post introduces an alpha feature in Kubernetes v1.33 called `StorageCapacityScoring`, which enhances pod scheduling by scoring nodes based on their storage capacity. This feature extends the kube-scheduler's VolumeBinding plugin, allowing it to use node storage capacity for scoring, which was previously only possible through a scheduler extender. It is particularly useful for provisioning node-local persistent volumes (PVs) by assigning them to nodes with the most available storage space, or for minimizing operational costs in cloud environments by selecting nodes with the least available storage. To enable this feature, users need to add `StorageCapacityScoring=true` to the kube-scheduler command line option `--feature-gates`. Configuration changes can prioritize nodes based on storage utilization using the `shape` parameter. The current feature will replace the deprecated `VolumeCapacityPriority`, which prioritized nodes with lower storage capacity, while `StorageCapacityScoring` prioritizes nodes with higher storage capacity by default.
👉 [Read more](https://kubernetes.io/blog/2025/04/30/kubernetes-v1-33-storage-capacity-scoring-feature/)

## 🔹 Spring Boot - Spring AI 1.0.0 M8 Released
The tech blog post discusses the release of Spring AI 1.0.0 M8, an additional milestone introduced to help developers transition smoothly before the RC1 release by retaining deprecated APIs alongside their replacements. Key changes in this release include enhancements to chat memory architecture, new template rendering features, improvements to MCP tool callback configurations, additional documentation on prompt engineering patterns, and vector store enhancements. Important deprecations involve updates to the ChatClient, prompt templating, and chat memory configurations. The post also acknowledges the contributions from various developers who helped with refactoring, bug fixes, and documentation enhancements.
👉 [Read more](https://spring.io/blog/2025/04/30/spring-ai-1-0-0-m8-released)

## 🔹 Docker - Update on the Docker DX extension for VS Code
The tech blog post discusses the latest updates to the Docker DX extension for Visual Studio Code. It highlights new features aimed at improving the authoring experience and outlines upcoming enhancements designed to streamline and enhance container workflows for developers.
👉 [Read more](https://www.docker.com/blog/docker-dx-extension-for-vs-code-update/)

## 🔹 Java - Announcing Jipher: Java Cryptographic Service Provider for FIPS Environments
The blog post announces the release of Oracle Jipher, a Java Cryptographic Service Provider designed for FIPS environments. Jipher packages an OpenSSL cryptographic module that has been validated under the Federal Information Processing Standards (FIPS) 140-2. This new provider allows Java developers to access cryptographic services using the standard Java Cryptography Architecture (JCA) framework, enhancing security and compliance in their applications.
👉 [Read more](https://inside.java/2025/04/30/jipher-release/)

## 🔹 Golang - More predictable benchmarking with testing.B.Loop
The blog post discusses improvements in benchmarking within the Go programming language, specifically with the introduction of `testing.B.Loop` in Go 1.24. This new feature aims to provide more predictable and reliable benchmark results by enhancing the way loops are handled during performance testing. By using `testing.B.Loop`, developers can achieve more consistent and accurate measurements in their benchmark tests, leading to more reliable performance insights for their Go applications.
👉 [Read more](https://go.dev/blog/testing-b-loop)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
The blog post announces that the Helm team will be attending KubeCon + CloudNativeCon EU 2025 in London from April 1 to 4. They are preparing for the release of Helm 4 later in the year and encourage attendees to engage with their maintainers during talk sessions and at the Helm booth in the Project Pavilion. The post provides details on Helm-related activities happening throughout the week.
👉 [Read more](https://helm.sh/blog/helm-at-kubecon-eu-25/)

