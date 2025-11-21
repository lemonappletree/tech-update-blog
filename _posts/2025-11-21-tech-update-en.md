# 🛠️ 2025-11-21 Tech Update Summary

## 🔹 Kubernetes - Ingress NGINX Retirement: What You Need to Know
The blog post discusses the upcoming retirement of Ingress NGINX, announced by Kubernetes SIG Network and the Security Response Committee. Best-effort maintenance will continue until March 2026, after which there will be no more updates, bug fixes, or security patches. Although existing deployments will remain functional, users are encouraged to migrate to alternatives like the Gateway API or other Ingress controllers listed in Kubernetes documentation. Ingress NGINX, once popular for its flexibility and features, faced maintenance challenges due to limited support and changing software expectations. Despite efforts, there was insufficient interest in maintaining or developing a replacement, leading to its planned retirement. Users are advised to initiate migration plans immediately to ensure continued security and functionality.
👉 [Read more](https://kubernetes.io/blog/2025/11/11/ingress-nginx-retirement/)

## 🔹 Spring Boot - A Bootiful Podcast: The legendary Sébastien Deleuze on all that's new and nice in Spring Framework 7
The blog post discusses a podcast episode featuring Sébastien Deleuze, a notable contributor to the Spring Framework. The episode focuses on the new features and improvements in Spring Framework 7, which are part of the recent Spring Boot 4.0 release. The podcast aims to provide insights into the latest advancements and how they enhance the Spring ecosystem. The post encourages listeners to explore the new release, available on Spring Initializr.
👉 [Read more](https://spring.io/blog/2025/11/20/a-bootiful-podcast-sebastien-deleuze)

## 🔹 Docker - Docker Model Runner Integrates vLLM for High-Throughput Inference
The blog post announces the integration of the vLLM inference engine and safetensors models into Docker Model Runner, enhancing its capabilities for high-throughput AI inference. This integration allows developers to leverage the existing Docker tooling they are familiar with to run and experiment with AI models more efficiently. The update aims to simplify the process for developers, aligning with Docker Model Runner's initial goal of ease of use in AI model experimentation.
👉 [Read more](https://www.docker.com/blog/docker-model-runner-integrates-vllm/)

## 🔹 Java - Java 26 Warns of Deep Reflection - Inside Java Newscast #101
The blog post discusses a new feature in Java 26 that will issue run-time warnings when a final field is altered through reflection, with the aim of eventually making such mutations illegal by default. This change is intended to enhance Java's integrity, particularly regarding the use of the final keyword, which will, in turn, improve maintainability, security, and performance. Although it is recommended to avoid mutating final fields, Java 26 introduces a permanent command-line option, --enable-final-field-mutation, allowing such mutations for specific modules. To facilitate the transition, a broader but temporary option, --illegal-final-field-mutation, has also been introduced.
👉 [Read more](https://inside.java/2025/11/20/newscast-101/)

## 🔹 Golang - Go’s Sweet 16
The blog post titled "Go’s Sweet 16" celebrates the 16th anniversary of the Go programming language. It highlights the journey and growth of Go since its inception, including its impact on software development and its vibrant community. The post reflects on the milestones achieved over the years and acknowledges the contributions of developers and users who have supported and advanced the language.
👉 [Read more](https://go.dev/blog/16years)

