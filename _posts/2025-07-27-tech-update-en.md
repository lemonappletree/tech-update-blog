# 🛠️ 2025-07-27 Tech Update Summary

## 🔹 Kubernetes - Post-Quantum Cryptography in Kubernetes
The blog post discusses the integration of Post-Quantum Cryptography (PQC) in Kubernetes, emphasizing the need for cryptographic algorithms that can withstand attacks from both classical and quantum computers. Quantum computers pose a threat to current cryptographic standards like RSA and ECC, making the adoption of PQC crucial. The article highlights the standardization of PQC algorithms by NIST, notably the Module-Lattice Key Encapsulation Mechanism (ML-KEM), which has been integrated into Kubernetes starting from version 1.33 via Go 1.24. This version supports hybrid post-quantum key exchanges using X25519MLKEM768 for TLS connections by default, enhancing Kubernetes' quantum resistance without major announcements or proposals. Challenges such as Go version mismatches, larger packet sizes for PQC keys, and the slower adoption of PQC digital signatures are also discussed. The blog concludes by noting that while PQC for key exchanges is progressing, digital signatures are still in the early stages of integration, and awareness of these issues is vital for maintaining Kubernetes' security.
👉 [Read more](https://kubernetes.io/blog/2025/07/18/pqc-in-k8s/)

## 🔹 Spring Boot - Spring Modulith 2.0 M1 released
The blog post announces the release of Spring Modulith 2.0 M1, which is based on the latest Spring Boot 4 M1 and Spring Framework 7.0 M7. A key feature of this release is the revamped Event Publication Registry, which addresses limitations in the previous version. The registry now includes new states such as "published," "processing," "failed," and "resubmitted," improving the ability to differentiate between states and support multi-instance deployments without distributed locking. The JDBC implementation supports the new event publication status model, while other store modules maintain compatibility. The release includes a staleness monitor to handle events stuck in certain states and introduces a new property namespace for configuration. Users are encouraged to try the JDBC-based registry, and existing applications can continue using the legacy schema by setting a specific property. The full change log is available online, and feedback is welcomed.
👉 [Read more](https://spring.io/blog/2025/07/26/spring-modulith-2-0-M1-released)

## 🔹 Docker - Docker MCP Catalog: Finding the Right AI Tools for Your Project
The blog post discusses the advancements in large language models (LLMs) from being simple text generators to becoming dynamic agents that can perform actions. This evolution has created a demand for a standardized method to securely enable these models to interact with external tools. The Model Context Protocol (MCP) addresses this need by transforming existing APIs into tools that can be accessed by AI. The post likely elaborates on how MCP works and its benefits for developers looking to integrate AI capabilities into their projects using Docker's MCP Catalog.
👉 [Read more](https://www.docker.com/blog/finding-the-right-ai-developer-tools-mcp-catalog/)

## 🔹 Java - JEP targeted to JDK 25: 520: JFR Method Timing &amp; Tracing
The blog post discusses JEP 520, which is aimed at JDK 25. This JEP introduces enhancements to Java Flight Recorder (JFR) focusing on method timing and tracing. The goal is to improve performance monitoring and analysis by providing more detailed insights into method execution times and call traces. This enhancement will help developers better understand application behavior and optimize performance. The post provides a link for further details on the proposed changes and their implications for JDK 25.
👉 [Read more](https://inside.java/2025/07/25/jep520-target-jdk25/)

## 🔹 Golang - The FIPS 140-3 Go Cryptographic Module
The blog post discusses the introduction of a native FIPS 140-3 compliant cryptographic module in the Go programming language. This update means that Go now includes built-in support for FIPS 140-3, a U.S. government standard for security requirements in cryptographic modules. This addition enhances Go's security features, making it more suitable for use in environments that require compliance with strict security standards. The blog provides details on how this new mode can be enabled and utilized by developers.
👉 [Read more](https://go.dev/blog/fips140)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
The blog post announces that the Helm team will be attending KubeCon + CloudNativeCon EU '25 in London from April 1 to 4. The team will be discussing the upcoming release of Helm 4 and engaging with attendees through talk sessions and at their booth in the Project Pavilion. The post invites readers to join the conversation and provides more details about Helm-related activities during the event.
👉 [Read more](https://helm.sh/blog/helm-at-kubecon-eu-25/)

