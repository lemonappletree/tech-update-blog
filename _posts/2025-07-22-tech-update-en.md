# 🛠️ 2025-07-22 Tech Update Summary

## 🔹 Kubernetes - Post-Quantum Cryptography in Kubernetes
The blog post discusses the integration of Post-Quantum Cryptography (PQC) in the Kubernetes ecosystem, emphasizing the importance of transitioning to PQC due to the potential threat posed by quantum computing to classical cryptographic systems like RSA and ECC. It introduces the concept of PQC, focusing on hybrid key exchange mechanisms in TLS that combine classical algorithms with PQC algorithms, such as the Module-Lattice Key Encapsulation Mechanism (ML-KEM). The post highlights the unexpected adoption of PQC in Kubernetes v1.33 due to its underlying use of Go 1.24, which supports hybrid PQC KEM by default. It also addresses potential issues like version mismatches between different Go versions, the larger packet sizes of PQC keys, and the current state of PQC digital signatures, which face challenges in terms of key size, performance, and toolchain support. The article concludes by noting the progress toward a quantum-safe Kubernetes environment, while acknowledging the need for further development and awareness of potential pitfalls.
👉 [Read more](https://kubernetes.io/blog/2025/07/18/pqc-in-k8s/)

## 🔹 Spring Boot - Spring AMQP 4.0 Milestone 3 Available
The tech blog post announces the release of the third milestone for Spring AMQP version 4.0.0, as well as the release of patch version 3.2.6. Key updates in this milestone include support for Jackson 3 with the deprecation of Jackson 2 components, the deprecation of JUnit 4 components, and improvements to the `BlockingQueueConsumer` during the shutdown phase. The post encourages readers to check the release notes for more details and invites them to reach out via GitHub issues if needed. Links to the project page, GitHub issues, contribution guidelines, and Stack Overflow help are provided.
👉 [Read more](https://spring.io/blog/2025/07/21/spring-amqp-4-0-0-m3-available)

## 🔹 Docker - Docker Unveils the Future of Agentic Apps at WeAreDevelopers
In the blog post titled "Docker Unveils the Future of Agentic Apps at WeAreDevelopers," Docker explores the concept of agentic applications. These are defined as applications that utilize Large Language Models (LLMs) to establish execution workflows based on specific goals, integrating with tools, data, and systems. The post discusses the challenges and innovations in building, testing, and deploying these applications, highlighting new elements introduced to the application stack to support this emerging technology.
👉 [Read more](https://www.docker.com/blog/wearedevelopers-docker-unveils-the-future-of-agentic-apps/)

## 🔹 Java - JEP targeted to JDK 25: 518: JFR Cooperative Sampling
The blog post discusses JEP 518, which is aimed at being included in JDK 25. The focus of this JEP is on JFR (Java Flight Recorder) Cooperative Sampling. This enhancement is designed to improve the efficiency and performance of data recording in Java applications by introducing a cooperative sampling mechanism. Cooperative sampling allows the system to better manage and reduce the overhead associated with data collection, leading to more efficient monitoring and analysis of Java applications. The post highlights the significance of this improvement for developers and the Java community as it aims to optimize performance without sacrificing the quality of data collected for profiling and diagnostics.
👉 [Read more](https://inside.java/2025/07/21/jep518-target-jdk25/)

## 🔹 Golang - The FIPS 140-3 Go Cryptographic Module
The blog post discusses the introduction of a built-in, native FIPS 140-3 compliant mode in the Go programming language. This addition ensures that Go's cryptographic library meets the stringent security requirements set by the Federal Information Processing Standards (FIPS). This compliance is crucial for developers working in regulated industries where adherence to such standards is mandatory. The post likely details the implementation process, benefits, and potential use cases for this new feature in Go, highlighting its significance for enhancing security in software development.
👉 [Read more](https://go.dev/blog/fips140)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
The blog post announces that the Helm team will be attending KubeCon + CloudNativeCon EU 2025 in London from April 1 to 4. The event will feature discussions about the upcoming Helm 4, which is set to be released later in the year. Attendees are encouraged to engage with Helm maintainers during talk sessions and visit the Helm booth in the Project Pavilion. The post provides additional details about Helm-related activities throughout the week.
👉 [Read more](https://helm.sh/blog/helm-at-kubecon-eu-25/)

