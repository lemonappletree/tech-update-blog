# 🛠️ 2025-09-14 Tech Update Summary

## 🔹 Kubernetes - Kubernetes v1.34: Autoconfiguration for Node Cgroup Driver Goes GA
The blog post discusses the new feature in Kubernetes v1.34, which has made the autoconfiguration of the node cgroup driver generally available (GA). Traditionally, configuring the correct cgroup driver was a challenge for Kubernetes users, as the kubelet and CRI implementations required manual configuration to use the same driver. The introduction of the feature gate `KubeletCgroupDriverFromCRI` in v1.28.0 allowed the kubelet to detect the cgroup driver automatically, based on the CRI implementation. This feature is now GA in Kubernetes 1.34.

Cluster administrators need to ensure their CRI implementation is updated: containerd needs to be v2.0.0 or later, and CRI-O should be v1.28.0 or later. Kubernetes is also deprecating support for containerd v1.y, with support ending in v1.36.0. A new detection mechanism via the `kubelet_cri_losing_support` metric helps administrators identify nodes using outdated containerd versions, prompting necessary upgrades to maintain compatibility with future Kubernetes versions.
👉 [Read more](https://kubernetes.io/blog/2025/09/12/kubernetes-v1-34-cri-cgroup-driver-lookup-now-ga/)

## 🔹 Spring Boot - Spring Cloud 2025.1.0-M2 (aka Oakwood) has been released
The blog post announces the release of Spring Cloud 2025.1.0-M2, also known as Oakwood. This milestone release is now available in Maven Central and details can be found in the release notes on GitHub. Notably, this version depends on Spring Boot 4.0.0-M2 and includes updates to various modules such as Spring Cloud OpenFeign, Config, Build, Stream, Netflix, Circuitbreaker, Contract, Commons, Consul, Gateway, Vault, Function, Dependencies, Task, Kubernetes, Bus, and Zookeeper, all updated to version 5.0.0-M2. The post encourages feedback via GitHub, Stack Overflow, or Twitter and provides instructions for setting up the release with Maven and Gradle.
👉 [Read more](https://spring.io/blog/2025/09/12/spring-cloud-2025-1-0-M2-aka-oakwood-has-been-released)

## 🔹 Docker - From Hallucinations to Prompt Injection: Securing AI Workflows at Runtime
The blog post "From Hallucinations to Prompt Injection: Securing AI Workflows at Runtime" discusses the importance of embedding runtime security in AI workflows to protect against potential vulnerabilities. It highlights how AI tools, while powerful, can be unpredictable and susceptible to exploitation. The article uses the example of prompting a large language model (LLM) to generate code, such as a Dockerfile or shell script, which appears correct but may contain hidden risks when executed. The post emphasizes the need for developers to implement security measures during runtime to ensure the safe use of AI agents.
👉 [Read more](https://www.docker.com/blog/secure-ai-agents-runtime-security/)

## 🔹 Java - All API Additions From Java 21 to 25 #RoadTo25
The tech blog post titled "All API Additions From Java 21 to 25 #RoadTo25" provides a comprehensive overview of the new API features introduced between Java versions 21 and 25. Key additions include scoped values, which likely enhance variable scoping capabilities; stream gatherers, which may offer new ways to handle data streams; an updated class-file API for improved manipulation and analysis of Java class files; and enhancements to the foreign function and memory API, potentially improving interoperability with non-Java code and memory management. Additionally, the post discusses new features and improvements in Javadoc, which could enhance documentation capabilities for developers. The blog offers a detailed look at these advancements, contributing to the evolving Java ecosystem.
👉 [Read more](https://inside.java/2025/09/09/roadto25-api/)

## 🔹 Golang - A new experimental Go API for JSON
The blog post discusses the introduction of new experimental APIs for JSON handling in Go 1.25. These APIs are part of the `encoding/json/jsontext` and `encoding/json/v2` packages. The objective of these new packages is to provide improved performance and flexibility in JSON encoding and decoding compared to the existing `encoding/json` package. The post likely covers the motivations behind these updates, potential benefits, and how developers can experiment with these new APIs in their Go projects.
👉 [Read more](https://go.dev/blog/jsonv2-exp)

## 🔹 Helm - Path To Releasing Helm v4
The blog post discusses the release of the first Alpha version of Helm v4, marking a significant step in its development. It outlines the current progress, future plans, and how the community can participate in the process. The post aims to engage the broader community in the development and testing of Helm v4 before its final release.
👉 [Read more](https://helm.sh/blog/path-to-helm-v4/)

