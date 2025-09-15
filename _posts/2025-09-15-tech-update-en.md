# 🛠️ 2025-09-15 Tech Update Summary

## 🔹 Kubernetes - Kubernetes v1.34: Autoconfiguration for Node Cgroup Driver Goes GA
The blog post discusses the general availability (GA) of automatic cgroup driver detection in Kubernetes v1.34. This feature addresses the previous challenge of manually configuring the cgroup driver in Kubernetes clusters, which could lead to misbehavior of the kubelet without clear error messages. The automated detection feature was introduced in v1.28.0 with the `KubeletCgroupDriverFromCRI` feature gate, allowing the kubelet to automatically determine the appropriate cgroup driver from the CRI implementation. This feature is now fully supported in Kubernetes v1.34.0.

For this feature to work, cluster administrators must ensure their CRI implementations are updated: containerd requires v2.0.0, and CRI-O requires v1.28.0. Additionally, the blog notes that Kubernetes is deprecating support for containerd v1.y, with v1.35 being the last release to support it. Administrators should upgrade to containerd v2.0 or later before upgrading to kubelet v1.36.0. A new metric, `kubelet_cri_losing_support`, helps detect nodes using soon-to-be-outdated containerd versions.
👉 [Read more](https://kubernetes.io/blog/2025/09/12/kubernetes-v1-34-cri-cgroup-driver-lookup-now-ga/)

## 🔹 Spring Boot - Spring Cloud 2025.1.0-M2 (aka Oakwood) has been released
The blog post announces the release of Spring Cloud 2025.1.0-M2, also known as Oakwood. This milestone release is now available on Maven Central, and detailed release notes can be accessed online. The release depends on Spring Boot 4.0.0-M2 and includes updates to various modules such as Spring Cloud OpenFeign, Config, Build, Stream, Netflix, Circuitbreaker, Contract, Commons, Consul, Gateway, Vault, Function, Dependencies, Task, Kubernetes, Bus, and Zookeeper, all updated to version 5.0.0-M2. The post encourages feedback via GitHub, Stack Overflow, or Twitter. It also provides instructions for integrating the release with Maven or Gradle projects.
👉 [Read more](https://spring.io/blog/2025/09/12/spring-cloud-2025-1-0-M2-aka-oakwood-has-been-released)

## 🔹 Docker - From Hallucinations to Prompt Injection: Securing AI Workflows at Runtime
The blog post titled "From Hallucinations to Prompt Injection: Securing AI Workflows at Runtime" discusses the importance of embedding runtime security in AI workflows to ensure safe development with AI agents. It highlights how AI tools, while powerful, can be unpredictable and vulnerable to exploitation. The post illustrates this with a scenario where a large language model (LLM) is prompted to generate code, such as a Dockerfile or shell script, which appears correct but may pose security risks when executed. The article emphasizes the need for developers to be vigilant and implement security measures to protect AI workflows from potential threats and attacks.
👉 [Read more](https://www.docker.com/blog/secure-ai-agents-runtime-security/)

## 🔹 Java - All API Additions From Java 21 to 25 #RoadTo25
The blog post titled "All API Additions From Java 21 to 25 #RoadTo25" provides an overview of the new API features introduced in Java versions 21 through 25. It covers several significant additions, including scoped values, which likely help manage data within specific execution contexts, and stream gatherers, which enhance data processing capabilities. The post also discusses updates to the class-file API, improvements to the foreign function and memory API, and enhancements to Javadoc. These updates reflect Java's ongoing evolution to improve functionality and developer experience.
👉 [Read more](https://inside.java/2025/09/09/roadto25-api/)

## 🔹 Golang - A new experimental Go API for JSON
The blog post discusses the experimental release of new JSON handling APIs in Go 1.25, specifically the `encoding/json/jsontext` and `encoding/json/v2` packages. These new APIs aim to improve JSON encoding and decoding functionality in Go, offering more robust and efficient handling of JSON data. The introduction of these packages is part of an effort to enhance the language's capabilities in dealing with JSON, addressing some of the limitations of the existing JSON support in Go. The blog post likely provides insights into the features and potential benefits of using these new packages for developers working with JSON in Go.
👉 [Read more](https://go.dev/blog/jsonv2-exp)

## 🔹 Helm - Path To Releasing Helm v4
The blog post discusses the release of the first Alpha version of Helm v4. It highlights that Helm v4 development is nearing completion and provides details on the current state of progress. The post also invites the broader community to participate and get involved in the development process. For more information, readers are encouraged to visit the provided link to the full blog post.
👉 [Read more](https://helm.sh/blog/path-to-helm-v4/)

