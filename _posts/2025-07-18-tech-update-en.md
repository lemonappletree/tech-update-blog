# 🛠️ 2025-07-18 Tech Update Summary

## 🔹 Kubernetes - Post-Quantum Cryptography in Kubernetes
The blog post discusses the significance of Post-Quantum Cryptography (PQC) in the context of Kubernetes, particularly in light of the potential threats posed by quantum computing to current cryptographic standards. PQC aims to develop cryptographic algorithms that are secure against both classical and quantum computers. The article emphasizes the urgency of transitioning to PQC algorithms, highlighting key exchange as an immediate priority due to the risk of future decryption by quantum computers.

The post examines the current state of PQC in Kubernetes, noting that as of version 1.33, Kubernetes supports hybrid post-quantum key exchange by default due to its use of Go 1.24. This version of Go includes support for the X25519MLKEM768 hybrid scheme, marking a significant step towards making Kubernetes quantum-safe.

However, challenges remain, such as potential issues with mismatched Go versions leading to fallback to classical cryptography, and the larger packet sizes required by PQC, which can cause network issues. The post also discusses the slower adoption of PQC digital signatures, which face hurdles like larger key sizes and performance issues.

Overall, the blog post underscores the importance of staying informed about PQC developments to ensure the long-term security of Kubernetes, while acknowledging the proactive steps already taken in integrating PQC key exchange mechanisms.
👉 [Read more](https://kubernetes.io/blog/2025/07/18/pqc-in-k8s/)

## 🔹 Spring Boot - A Bootiful Podcast: Spring legends Tasha Isenberg and Jason Konicki
In the tech blog post titled "A Bootiful Podcast: Spring legends Tasha Isenberg and Jason Konicki," the author shares a conversation with Spring experts Tasha Isenberg and Jason Konicki. The podcast episode features insights and discussions about their experiences and contributions to the Spring community. Additionally, the author mentions a conversation with Arjen Poutsma, an API expert, and encourages readers to explore his insights and consultancy services through his website, poutsma-principles.com.
👉 [Read more](https://spring.io/blog/2025/07/17/a-bootiful-podcast-jason-and-tasha)

## 🔹 Docker - GoFiber v3 + Testcontainers: Production-like Local Dev with Air
The blog post discusses the challenges of local development when applications depend on external services, such as databases or message queues, which can result in fragile scripts and inconsistent environments. The new version of Fiber, v3, combined with Testcontainers, addresses these issues by integrating real service dependencies into the application's lifecycle. This integration makes the development process more manageable, reproducible, and user-friendly for developers. The post highlights the upcoming release of Fiber v3, which introduces significant improvements to enhance local development experiences by leveraging these tools.
👉 [Read more](https://www.docker.com/blog/go-local-dev-fiber-v3-testcontainers/)

## 🔹 Java - Java Gets a JSON API - Inside Java Newscast #95
The blog post discusses the introduction of a JSON API for Java, highlighting its necessity given JSON's widespread use as a data exchange format. Java, known for being a comprehensive language with built-in tools, aims to include a native JSON API to align with its "batteries included" philosophy. The episode covers an OpenJDK email that initiates the exploration of developing this API, emphasizing the importance of integrating JSON capabilities directly into the Java ecosystem.
👉 [Read more](https://inside.java/2025/07/17/newscast-95/)

## 🔹 Golang - The FIPS 140-3 Go Cryptographic Module
The blog post discusses the introduction of a native FIPS 140-3 compliant mode in the Go programming language. This update allows developers to utilize cryptographic modules that meet the Federal Information Processing Standards (FIPS) 140-3 requirements directly within Go. This integration aims to streamline the development process for applications that need to adhere to these strict security standards, ensuring that Go remains a viable option for developing secure and compliant software solutions.
👉 [Read more](https://go.dev/blog/fips140)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
The blog post discusses the Helm team's participation in KubeCon + CloudNativeCon EU 2025, taking place in London, UK, from April 1 to 4. The team will be discussing the upcoming release of Helm 4, and attendees can engage with Helm maintainers during talk sessions and visit the Helm booth in the Project Pavilion. The post encourages attendees to join the conversation and provides more details on Helm-related activities throughout the event.
👉 [Read more](https://helm.sh/blog/helm-at-kubecon-eu-25/)

