# 🛠️ 2025-07-26 Tech Update Summary

## 🔹 Kubernetes - Post-Quantum Cryptography in Kubernetes
The blog post discusses the impact of quantum computing on cryptography, emphasizing the need for Post-Quantum Cryptography (PQC) in systems like Kubernetes. Quantum computers, though theoretical for many uses, could break current cryptographic standards, making PQC crucial for long-term security. PQC algorithms, designed to withstand quantum attacks, are being standardized, with NIST's ML-KEM being an example. The blog explains the urgency of migrating to PQC, especially for key exchanges in TLS, due to the potential risk of encrypted data being decrypted in the future. While digital signatures also need migration, they pose a lesser immediate risk. The post highlights that support for PQC is improving, with Go, browsers, and OpenSSL adopting PQC algorithms. Kubernetes, built with Go, supports PQC by default from version 1.33. However, issues like Go version mismatches and larger packet sizes pose challenges. While PQC KEMs are advancing, PQC digital signatures face hurdles like larger key sizes and slower performance. The blog concludes that Kubernetes is progressing towards quantum safety, though further awareness and development are needed for comprehensive PQC adoption.
👉 [Read more](https://kubernetes.io/blog/2025/07/18/pqc-in-k8s/)

## 🔹 Spring Boot - Spring Modulith 1.4.2 and 1.3.8 released
The blog post announces the release of Spring Modulith versions 1.4.2 and 1.3.8. These updates include dependency upgrades to the latest versions of Spring Boot and Framework. Version 1.4.2 introduces more detailed application module metadata, which is generated into `application-modules.json` using AOT support or through the `Documenter` API. This enhancement allows Sonargraph, a tool for defining application architectures, to integrate with Spring Modulith applications. More details about these releases can be found in the full changelogs linked in the post.
👉 [Read more](https://spring.io/blog/2025/07/25/spring-modulith-1-4-2-and-1-3-8-released)

## 🔹 Docker - Docker MCP Catalog: Finding the Right AI Tools for Your Project
The blog post discusses the evolution of large language models (LLMs) from simply generating text to becoming dynamic agents that can perform actions. This progression necessitates a standardized method for these models to interact with external tools securely. The Model Context Protocol (MCP) is introduced as a solution, enabling existing APIs to become accessible tools for AI. The post details how MCP facilitates this transformation, helping developers find the right AI tools for their projects.
👉 [Read more](https://www.docker.com/blog/finding-the-right-ai-developer-tools-mcp-catalog/)

## 🔹 Java - JEP targeted to JDK 25: 520: JFR Method Timing &amp; Tracing
The blog post discusses a new JEP (JDK Enhancement Proposal) numbered 520, which is aimed at JDK 25. This proposal introduces JFR (Java Flight Recorder) Method Timing and Tracing. The enhancement focuses on improving the capabilities of JFR by adding detailed method timing and tracing features. This will allow developers to gather more precise performance data and better analyze the execution of Java methods, which can lead to improved application performance and debugging capabilities. The post likely elaborates on the specific benefits and technical details of this new feature, although the summary provided does not go into these specifics.
👉 [Read more](https://inside.java/2025/07/25/jep520-target-jdk25/)

## 🔹 Golang - The FIPS 140-3 Go Cryptographic Module
The blog post discusses the introduction of a FIPS 140-3 compliant cryptographic module in the Go programming language. This new feature provides a built-in, native mode that adheres to the Federal Information Processing Standard (FIPS) 140-3, ensuring enhanced security for cryptographic operations. This advancement is significant for developers and organizations that require compliance with stringent security standards for cryptographic modules. The post likely covers the implementation details, benefits, and potential use cases for this new capability in Go.
👉 [Read more](https://go.dev/blog/fips140)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
The blog post announces that the Helm team will be attending KubeCon + CloudNativeCon EU 2025 in London from April 1-4. They highlight that Helm 4 is in development and encourage attendees to engage with Helm maintainers during talk sessions and at the Helm booth in the Project Pavilion. The post provides details on all Helm-related activities during the event.
👉 [Read more](https://helm.sh/blog/helm-at-kubecon-eu-25/)

