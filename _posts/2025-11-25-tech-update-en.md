# 🛠️ 2025-11-25 Tech Update Summary

## 🔹 Kubernetes - Ingress NGINX Retirement: What You Need to Know
The blog post discusses the planned retirement of Ingress NGINX by Kubernetes SIG Network and the Security Response Committee. The decision is made to prioritize security within the ecosystem. Maintenance for Ingress NGINX will continue until March 2026, after which there will be no further updates, bug fixes, or security patches. Existing deployments will remain functional, and installation artifacts will still be accessible. Users are advised to migrate to alternatives such as the Gateway API or other Ingress controllers listed in the Kubernetes documentation. The post highlights the historical significance and challenges of maintaining Ingress NGINX, noting insufficient support for its sustainability. The community is encouraged to transition away from Ingress NGINX to ensure future security and functionality.
👉 [Read more](https://kubernetes.io/blog/2025/11/11/ingress-nginx-retirement/)

## 🔹 Spring Boot - Towards Spring Tools 5 - Ready for Boot 4 and Framework 7
The blog post discusses the upcoming release of Spring Tools 5, which is set to support the new features of Spring Framework 7 and Spring Boot 4. Scheduled for general availability on December 10th, with release candidates already available, Spring Tools 5 will include several enhancements:

1. **API Versioning**: The new version supports API versioning in Spring Framework 7, offering features like codelens for controllers, request mapping symbols, and validation for versioning strategies.

2. **Bean Registrars**: Improved support for functional bean definitions is provided through the bean registrar mechanism, allowing structured programmatic bean definitions.

3. **AOT Repositories**: The integration with Spring Data's ahead-of-time compiled repositories will show SQL query details directly in the source code and facilitate navigation between repository interfaces and generated code.

4. **JSPECIFY Annotations**: Automatic configuration of JSpecify annotations for null analysis is supported, particularly in Eclipse, with plans to extend this to other environments like Visual Studio Code.

The post invites users to try the release candidates and mentions future blog posts will explore more features of Spring Tools 5, including its integration with AI tools.
👉 [Read more](https://spring.io/blog/2025/11/24/towards-spring-tools-5-part1)

## 🔹 Docker - Security that moves fast: Docker’s response to Shai Hulud 2.0
The blog post discusses Docker's rapid response to the Shai Hulud 2.0 attack, a significant npm supply chain attack detected on November 21, 2025. This attack compromised over 25,000 GitHub repositories in just 72 hours, impacting packages from major organizations such as Zapier, ENS Domains, PostHog, and Postman. The malware's self-propagating nature allowed it to spread quickly across the supply chain. Docker's response focused on addressing the threat swiftly to mitigate its impact and protect affected systems.
👉 [Read more](https://www.docker.com/blog/security-that-moves-fast-dockers-response-to-shai-hulud-2-0/)

## 🔹 Java - JEP targeted to JDK 26: 525: Structured Concurrency (6th Preview)
The blog post discusses the targeting of JEP 525: Structured Concurrency for JDK 26, marking its sixth preview. Structured Concurrency aims to simplify concurrent programming by managing multiple tasks in a structured and coordinated manner, enhancing reliability and maintainability. The JEP continues to evolve based on feedback and aims to provide developers with more robust tools for handling concurrency in Java applications.
👉 [Read more](https://inside.java/2025/11/24/jep525-target-jdk26/)

## 🔹 Golang - Go’s Sweet 16
The blog post titled "Go’s Sweet 16" celebrates the 16th anniversary of the Go programming language. It reflects on Go's journey since its inception, highlighting key milestones and achievements over the years. The post may also discuss the language's impact on the software development community, its growing popularity, and future prospects for Go.
👉 [Read more](https://go.dev/blog/16years)

