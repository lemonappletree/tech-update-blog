# 🛠️ 2025-10-06 Tech Update Summary

## 🔹 Kubernetes - Announcing Changed Block Tracking API support (alpha)
The blog post announces the alpha support for a Changed Block Tracking API, designed to enhance Kubernetes' storage ecosystem. This feature allows CSI storage drivers to identify modified blocks in PersistentVolume snapshots, leading to faster and more efficient backup operations. Changed block tracking eliminates the need for full volume scans during backups by identifying changes at the block level, focusing only on the modified data. This API is currently available only for block volumes, not file volumes. The post outlines the benefits, including reduced backup windows, lower resource utilization, and decreased storage costs. It also details the components and implementation requirements for storage providers and backup solutions. The Kubernetes team aims to advance this feature to beta status based on user feedback. The blog provides resources for further reading and invites community involvement in the project.
👉 [Read more](https://kubernetes.io/blog/2025/09/25/csi-changed-block-tracking/)

## 🔹 Spring Boot - Spring Cloud 2025.1.0-M3 (aka Oakwood) has been released
The tech blog post announces the release of Spring Cloud 2025.1.0-M3, also known as Oakwood, which is now available in the Spring Milestone repository. This release, which relies on Spring Boot 4.0.0-M3, includes several notable updates and changes across various Spring Cloud components. Key updates include the discontinuation of certain Spring Cloud Function modules, upgrades to the Kubernetes Java Client and Fabric8 Kubernetes Client, and property migration in Spring Cloud Contract. Additionally, Resilience4j has been upgraded to version 2.3.0 in Spring Cloud Circuitbreaker, and a new LoadBalancer API versioning support is added in Spring Cloud Commons. The post provides links to release notes and issues for each module and encourages feedback through GitHub, Gitter, Stack Overflow, and Twitter. It also includes instructions for getting started with Maven and Gradle.
👉 [Read more](https://spring.io/blog/2025/10/03/spring-cloud-2025-1-0-M3-aka-oakwood-has-been-released)

## 🔹 Docker - From Shell Scripts to Science Agents: How AI Agents Are Transforming Research Workflows
The blog post titled "From Shell Scripts to Science Agents: How AI Agents Are Transforming Research Workflows" describes the evolving role of AI agents in streamlining and enhancing research processes. It paints a picture of a typical researcher juggling multiple tasks and tools, such as shell scripts, Jupyter notebooks, and Excel sheets, to manage complex workflows like running protein folding models and parsing experimental data. AI agents are highlighted as transformative tools that can automate and optimize these workflows, potentially reducing the manual effort and allowing researchers to focus more on scientific discovery rather than administrative tasks. The post suggests that AI is playing an increasingly important role in facilitating more efficient and effective research environments.
👉 [Read more](https://www.docker.com/blog/ai-science-agents-research-workflows/)

## 🔹 Java - The Inside Java Newsletter: Java 25 is Live!
The Inside Java Newsletter for September 2025 highlights a range of technical videos centered around Java 25. It also provides updates on Java User Groups, developer events, learning resources, community podcasts, and contributions from the Java Platform Group. The newsletter encourages readers to visit learn.java, dev.java, and inside.java for a variety of multimedia content tailored for developers, learners, educators, and customers. Additionally, it invites readers to explore archived editions, subscribe for future updates, and share the newsletter with friends.
👉 [Read more](https://inside.java/2025/10/03/inside-java-newsletter/)

## 🔹 Golang - Flight Recorder in Go 1.25
The blog post discusses the introduction of a new diagnostic tool called flight recording in Go version 1.25. This tool is designed to help developers capture and analyze the state of a Go program over time, aiding in debugging and performance optimization. The post likely elaborates on how flight recording works, its benefits, and how developers can utilize it to enhance their Go programming projects. For more detailed information, readers are encouraged to visit the full post on the Go blog.
👉 [Read more](https://go.dev/blog/flight-recorder)

## 🔹 Helm - Path To Releasing Helm v4
The blog post discusses the release of the first Alpha version of Helm v4, marking a significant milestone in its development. With Helm v4 nearing completion, the post provides insights into the ongoing development process and encourages the broader community to participate in its progression. The blog aims to keep users informed about the current status and future plans for Helm v4, inviting community involvement in shaping the final release.
👉 [Read more](https://helm.sh/blog/path-to-helm-v4/)

