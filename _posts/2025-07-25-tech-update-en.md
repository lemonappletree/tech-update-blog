# 🛠️ 2025-07-25 Tech Update Summary

## 🔹 Kubernetes - Post-Quantum Cryptography in Kubernetes
The blog post discusses the impact of quantum computing on cryptography, emphasizing the need for Post-Quantum Cryptography (PQC) to secure systems against potential quantum attacks. In particular, it focuses on the adoption of PQC within the Kubernetes ecosystem. The post explains that quantum computers could break current cryptographic standards, prompting the shift towards PQC algorithms, which are resistant to both classical and quantum attacks. It highlights the importance of migrating Key Exchange Mechanisms (KEMs) to PQC, as these are critical for securing communications. The article notes that Kubernetes v1.33, using Go 1.24, supports hybrid post-quantum key exchanges by default, marking a significant step towards quantum-safe Kubernetes. However, it also discusses challenges such as Go version mismatches leading to cryptographic downgrades and issues with packet sizes due to larger PQC keys. While PQC KEMs are being adopted, PQC digital signatures face hurdles like larger key sizes and performance issues, with widespread integration still in progress. The post concludes that while Kubernetes has made strides towards post-quantum security, continued awareness and adaptation are necessary to ensure long-term security.
👉 [Read more](https://kubernetes.io/blog/2025/07/18/pqc-in-k8s/)

## 🔹 Spring Boot - A Bootiful Podcast: José Paumard, Java developer advocate and professor
In this tech blog post titled "A Bootiful Podcast: José Paumard, Java developer advocate and professor," the host engages in a conversation with José Paumard, a renowned computer science professor and Java developer advocate. Recorded at Devoxx UK 2025, the discussion covers topics related to Java and its ecosystem, providing insights and expert perspectives from Paumard.
👉 [Read more](https://spring.io/blog/2025/07/24/a-bootiful-podcast-jose-paumard)

## 🔹 Docker - Docker MCP Catalog: Finding the Right AI Tools for Your Project
The blog post discusses the evolving role of large language models (LLMs) as they transition from simple text generators to more complex agents capable of performing actions. This evolution creates a need for a standardized protocol that allows these models to interact with external tools securely. The Model Context Protocol (MCP) is introduced as a solution that enables existing APIs to become accessible to AI. The post highlights the importance of MCP in finding the right AI tools for projects and how it facilitates the integration of AI capabilities with various APIs.
👉 [Read more](https://www.docker.com/blog/finding-the-right-ai-developer-tools-mcp-catalog/)

## 🔹 Java - A Sneak Peek at the Stable Values API
The blog post introduces the Stable Values API, which addresses the limitations of the `@Stable` annotation in Java. Previously, the `@Stable` annotation could only be used internally within JDK classes to mark fields or array elements that change at most once, enhancing performance, energy efficiency, and flexibility. However, this annotation was not accessible to Java application developers. The Stable Values API solves this issue by providing safe wrappers around the `@Stable` annotation, making its benefits available to regular Java developers and third-party library developers. This API allows for the creation of lazy Lists and Maps with performance similar to constant values.
👉 [Read more](https://inside.java/2025/07/22/javaone-stablevalues/)

## 🔹 Golang - The FIPS 140-3 Go Cryptographic Module
The blog post discusses the introduction of a FIPS 140-3 compliant cryptographic module in the Go programming language. This new feature allows developers to utilize a built-in, native mode for cryptographic operations that adhere to the FIPS 140-3 standard, which is crucial for ensuring security and compliance in specific industries. The integration simplifies the process for developers needing to meet these stringent security requirements.
👉 [Read more](https://go.dev/blog/fips140)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
The blog post announces that the Helm team will be attending KubeCon + CloudNativeCon EU 2025 in London from April 1 to 4. They are preparing to release Helm 4 later this year and invite attendees to join discussions with Helm maintainers at their talk sessions and at the Helm booth in the Project Pavilion. The post includes more details on Helm-related activities throughout the week.
👉 [Read more](https://helm.sh/blog/helm-at-kubecon-eu-25/)

