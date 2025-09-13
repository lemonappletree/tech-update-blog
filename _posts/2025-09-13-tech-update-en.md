# 🛠️ 2025-09-13 Tech Update Summary

## 🔹 Kubernetes - Kubernetes v1.34: Autoconfiguration for Node Cgroup Driver Goes GA
The blog post discusses the new Kubernetes v1.34 release, highlighting the general availability (GA) of the autoconfiguration feature for the node cgroup driver. Previously, configuring the correct cgroup driver was challenging for users, as mismatched configurations between kubelet and CRI implementations could cause issues. The new feature, initially introduced in v1.28.0, automates the detection of the correct cgroup driver by enabling the `KubeletCgroupDriverFromCRI` feature gate. This requires using newer versions of CRI implementations like containerd v2.0.0 or CRI-O v1.28.0. Additionally, Kubernetes announces the deprecation of support for containerd v1.y, with the last supported version being Kubernetes v1.35. Post v1.35, administrators should ensure containerd is upgraded to v2.0 or later to meet new requirements, which can be monitored using the `kubelet_cri_losing_support` metric.
👉 [Read more](https://kubernetes.io/blog/2025/09/12/kubernetes-v1-34-cri-cgroup-driver-lookup-now-ga/)

## 🔹 Spring Boot - Spring Cloud 2025.1.0-M2 (aka Oakwood) has been released
The blog post announces the release of Spring Cloud 2025.1.0-M2, also known as Oakwood. This milestone release is available on Maven Central and is compatible with Spring Boot 4.0.0-M2. The blog highlights updates to multiple Spring Cloud modules, including Spring Cloud OpenFeign, Config, Build, Stream, Netflix, Circuitbreaker, Contract, Commons, Consul, Gateway, Vault, Function, Dependencies, Task, Kubernetes, Bus, and Zookeeper, all updated to version 5.0.0-M2, except Kubernetes, which is at 3.3.0-M1. The post encourages feedback on GitHub, Stack Overflow, and Twitter. It also provides instructions for getting started with Maven and Gradle using BOM (Bill of Materials) for dependency management.
👉 [Read more](https://spring.io/blog/2025/09/12/spring-cloud-2025-1-0-M2-aka-oakwood-has-been-released)

## 🔹 Docker - From Hallucinations to Prompt Injection: Securing AI Workflows at Runtime
The blog post titled "From Hallucinations to Prompt Injection: Securing AI Workflows at Runtime" discusses the importance of embedding runtime security in AI workflows to prevent exploitation and unpredictability. It highlights that while AI tools are powerful, they can also become attack surfaces. For example, an AI-generated Dockerfile or shell script might seem correct but could lead to vulnerabilities when executed. The post emphasizes the need for developers to integrate security measures directly within AI workflows to build safely with AI agents.
👉 [Read more](https://www.docker.com/blog/secure-ai-agents-runtime-security/)

## 🔹 Java - All API Additions From Java 21 to 25 #RoadTo25
The blog post titled "All API Additions From Java 21 to 25 #RoadTo25" provides an overview of the new API features introduced between Java versions 21 and 25. It highlights several key additions, including scoped values, which offer a new way to manage data within a specific scope, and stream gatherers, which enhance the functionality of streams in Java. The post also discusses updates to the class-file API, improvements in the foreign function and memory API, which facilitate better interaction with non-Java code, and enhancements to Javadoc, the documentation tool. These updates aim to improve the Java programming experience by offering more robust and versatile tools for developers.
👉 [Read more](https://inside.java/2025/09/09/roadto25-api/)

## 🔹 Golang - A new experimental Go API for JSON
The blog post discusses the introduction of experimental support in Go 1.25 for two new packages: `encoding/json/jsontext` and `encoding/json/v2`. These packages aim to improve JSON handling in the Go programming language. The update is part of an ongoing effort to enhance the language's capabilities and performance when working with JSON data. The post likely details the features and potential benefits of these new packages, encouraging developers to try them out and provide feedback.
👉 [Read more](https://go.dev/blog/jsonv2-exp)

## 🔹 Helm - Path To Releasing Helm v4
The blog post announces the release of the first Alpha version for Helm v4 and discusses the final stages of its development. It provides details about the progress towards the official release and invites the broader community to participate and contribute to the process. The post is aimed at keeping users informed about the latest developments and encouraging community involvement in shaping the new version.
👉 [Read more](https://helm.sh/blog/path-to-helm-v4/)

