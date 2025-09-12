# 🛠️ 2025-09-12 Tech Update Summary

## 🔹 Kubernetes - Kubernetes v1.34: Mutable CSI Node Allocatable Graduates to Beta
The blog post announces that the functionality allowing CSI drivers to update information about attachable volume count on nodes has moved to Beta in Kubernetes v1.34, after being introduced in Alpha in v1.33. This enhancement aims to improve the accuracy of stateful pod scheduling by preventing failures due to outdated volume capacity information. Traditionally, CSI drivers reported static maximum volume attachment limits, which could lead to scheduling issues. The new feature allows these limits to be updated dynamically at runtime through periodic and reactive updates. To use this feature, the `MutableCSINodeAllocatableCount` feature gate must be enabled in the `kube-apiserver` and `kubelet` components. An example configuration is provided for setting periodic updates every 60 seconds. Immediate updates can also occur when attachment operations fail due to resource exhaustion. The post encourages users to enable the feature and provide feedback to help evolve it towards General Availability.
👉 [Read more](https://kubernetes.io/blog/2025/09/11/kubernetes-v1-34-mutable-csi-node-allocatable-count/)

## 🔹 Spring Boot - A Bootiful Podcast: Purnima Padmanabhan, General Manager, Tanzu Division, Broadcom
The blog post summarizes an episode of "A Bootiful Podcast" featuring Purnima Padmanabhan, the General Manager of the Tanzu Division at Broadcom. The discussion covers topics such as artificial intelligence (AI) and the capabilities of the Tanzu platform. The podcast episode was recorded live during the SpringOne 2025 event.
👉 [Read more](https://spring.io/blog/2025/09/11/a-bootiful-podcast-purnima-padmanabhan)

## 🔹 Docker - From Hallucinations to Prompt Injection: Securing AI Workflows at Runtime
The blog post titled "From Hallucinations to Prompt Injection: Securing AI Workflows at Runtime" discusses the challenges of securing AI workflows during runtime. It highlights how AI tools, while powerful, can be unpredictable and susceptible to exploitation. The article emphasizes the importance of embedding runtime security measures when building with AI agents. Developers are advised to be cautious, as seemingly correct outputs from AI models, like Dockerfiles or shell scripts, can introduce vulnerabilities if not properly secured. The post likely provides insights and strategies on how to safeguard AI-driven development environments from potential threats.
👉 [Read more](https://www.docker.com/blog/secure-ai-agents-runtime-security/)

## 🔹 Java - All API Additions From Java 21 to 25 #RoadTo25
The blog post titled "All API Additions From Java 21 to 25 #RoadTo25" provides an overview of the new API features introduced in Java versions 21 through 25. It highlights several key additions, including:

1. **Scoped Values** - A new feature that provides enhanced control over the scope of variables and values.
2. **Stream Gatherers** - Enhancements to the Stream API for more efficient data processing and collection.
3. **Class-file API** - Improvements to the API dealing with Java class files, facilitating better manipulation and analysis.
4. **Foreign Function and Memory API** - Updates that allow Java programs to interact more seamlessly with native code and memory, enhancing interoperability.
5. **Javadoc Additions** - Enhancements to Javadoc for better documentation and usability.

The post is part of a series exploring the evolution of Java APIs leading up to version 25.
👉 [Read more](https://inside.java/2025/09/09/roadto25-api/)

## 🔹 Golang - A new experimental Go API for JSON
The blog post discusses the introduction of experimental support for new JSON handling packages in Go 1.25. These packages, `encoding/json/jsontext` and `encoding/json/v2`, aim to enhance JSON processing capabilities in the Go programming language. The new API is designed to improve performance, add more functionality, and provide a more intuitive interface for developers working with JSON data in Go applications. The post likely provides details on the features and improvements brought by these experimental packages and how they can be utilized by Go developers.
👉 [Read more](https://go.dev/blog/jsonv2-exp)

## 🔹 Helm - Path To Releasing Helm v4
The blog post discusses the release of the first Alpha version of Helm v4. It highlights that Helm v4's development is nearing completion and provides information on the current progress. The post also encourages community involvement, offering details on how people can participate and contribute to the project as it moves towards the final release.
👉 [Read more](https://helm.sh/blog/path-to-helm-v4/)

