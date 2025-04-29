# 🛠️ 2025-04-29 Tech Update Summary

## 🔹 Kubernetes - Kubernetes v1.33: HorizontalPodAutoscaler Configurable Tolerance
The blog post discusses a new alpha feature in Kubernetes v1.33, which allows for configurable tolerance in Horizontal Pod Autoscaling (HPA). Previously, the tolerance for triggering scaling actions was a fixed 10% across the cluster, but now users can configure it to better suit their needs. This feature is beneficial for large deployments where a 10% tolerance could lead to significant changes in the number of pods. Users can set different tolerances for scaling up and scaling down, enabling more responsive scaling to demand spikes and reducing unnecessary fluctuations. To use this feature, the `HPAConfigurableTolerance` feature gate must be enabled, and the desired tolerances can be set in the `spec.behavior.scaleDown` and `spec.behavior.scaleUp` fields of the HPA configuration. More detailed technical information can be found in Kubernetes Enhancement Proposal (KEP) 4951.
👉 [Read more](https://kubernetes.io/blog/2025/04/28/kubernetes-v1-33-hpa-configurable-tolerance/)

## 🔹 Spring Boot - Spring Boot 3.5.0-RC1 available now
The blog post announces the release of Spring Boot 3.5.0-RC1, now available for download. This release includes 133 enhancements, documentation improvements, dependency upgrades, and bug fixes. Key features include support for Docker's credential stores, improved configuration property binding performance, annotation-based filter and servlet registration, auto-configuration for bean initialization, and properties for global WebClient configuration. The post encourages contributors to get involved by checking the "ideal for contribution" tag in the issue repository and directs users with questions to Stack Overflow. Additional resources provided include links to the project page, GitHub repository, and documentation.
👉 [Read more](https://spring.io/blog/2025/04/25/spring-boot-3-5-0-RC1-available-now)

## 🔹 Docker - How to build and deliver an MCP server for production
The blog post discusses the growing interest and demand among developers to build, share, and run tools using the Model Context Protocol (MCP) with AI agents, known as Agentic AI. Since the introduction of MCP in December 2024, developers have been eager to implement this new specification to enhance their AI tool development. The blog provides insights into how to construct and deploy an MCP server for production environments, likely using Docker, based on the link provided.
👉 [Read more](https://www.docker.com/blog/build-to-prod-mcp-servers-with-docker/)

## 🔹 Java - Finalizing the Java On-ramp - Inside Java Newscast #90
The tech blog post titled "Finalizing the Java On-ramp - Inside Java Newscast #90" discusses significant changes coming in the Java 25 release. The episode of the Inside Java Newscast highlights the finalization of the "Paving the On-ramp" feature set, which aims to make Java more accessible. Additionally, it introduces a new website, lear.java, which is designed to support individuals learning Java and educators teaching the language.
👉 [Read more](https://inside.java/2025/04/24/ijn-ep-90/)

## 🔹 Golang - More predictable benchmarking with testing.B.Loop
The blog post discusses improvements in benchmarking for the Go programming language with the introduction of `testing.B.Loop` in Go 1.24. This new feature aims to provide more predictable and consistent benchmarking results. The update focuses on better handling of benchmark loops, allowing developers to achieve more accurate performance measurements for their code. This improvement is particularly beneficial for developers who rely on precise benchmarking to optimize their applications.
👉 [Read more](https://go.dev/blog/testing-b-loop)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
The blog post announces that the Helm team will be attending KubeCon + CloudNativeCon EU 2025 in London from April 1-4. The team is working on Helm 4, which is set to be released later in the year. Attendees are encouraged to participate in discussions with the Helm maintainers during talk sessions and visit the Helm booth in the Project Pavilion. The post provides details on all Helm-related activities scheduled for the week.
👉 [Read more](https://helm.sh/blog/helm-at-kubecon-eu-25/)

