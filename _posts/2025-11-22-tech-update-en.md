# 🛠️ 2025-11-22 Tech Update Summary

## 🔹 Kubernetes - Ingress NGINX Retirement: What You Need to Know
The blog post announces the upcoming retirement of Ingress NGINX by Kubernetes SIG Network and the Security Response Committee to ensure ecosystem safety and security. Maintenance will continue until March 2026, after which no further updates, bug fixes, or security patches will be provided. Current deployments will remain functional, and installation artifacts will still be accessible. Users are advised to transition to alternatives like the Gateway API, the modern replacement for Ingress, or other Ingress controllers listed in Kubernetes documentation. Ingress NGINX faced maintenance challenges due to limited support and changing expectations about cloud-native software, leading to its retirement decision. The community and maintainers are thanked for their contributions, and users are urged to start migrating to other solutions to ensure continued functionality and security.
👉 [Read more](https://kubernetes.io/blog/2025/11/11/ingress-nginx-retirement/)

## 🔹 Spring Boot - Spring Modulith 2.0 GA, 1.4.5, and 1.3.11 released
The blog post announces the release of Spring Modulith 2.0, marking a significant milestone with major new features and enhancements based on lessons learned from its first generation. Key updates include an overhaul of the event publication lifecycle with support for various databases (Neo4j, MongoDB, JDBC, JPA), application-module-specific Flyway migrations, serialized execution of event externalization, and support for Jackson 3 in event serialization. Additionally, it introduces startup verification of application module structures, migration to jSpecify for nullness verification, and other improvements. The release also removes the deprecated `@ApplicationEventListener` annotation and updates baselines to Spring Boot 4 and Framework 7. Bugfix releases for versions 1.4.5 and 1.3.11 are also available. More detailed information about the features is promised for future posts. For more details, readers can refer to the full changelog.
👉 [Read more](https://spring.io/blog/2025/11/21/spring-modulith-2-0-ga-1-4-5-and-1-3-11-released)

## 🔹 Docker - The Rising Importance of Governance at SwampUP Berlin 2025
The blog post discusses the Docker team's participation in the JFrog SwampUP Berlin 2025 event, held from November 12-14. The team engaged in various activities, including attending technical sessions, hosting a fireside chat, and interacting with attendees. The post expresses gratitude to JFrog for organizing the event and highlights key takeaways related to software governance from the event.
👉 [Read more](https://www.docker.com/blog/the-rising-importance-of-governance-at-swampup-berlin-2025/)

## 🔹 Java - Java 26 Warns of Deep Reflection - Inside Java Newscast #101
The blog post discusses a new feature in Java 26 that will generate run-time warnings when a final field is altered using reflection. This is a preparatory step towards a future update that will prohibit such modifications by default to enhance the integrity of Java's final keyword. This change is expected to positively impact maintainability, security, and performance. The post advises against mutating final fields but introduces a permanent command-line option, --enable-final-field-mutation, for allowing such mutations in specific modules. Additionally, a temporary option, --illegal-final-field-mutation, has been introduced to assist with the transition.
👉 [Read more](https://inside.java/2025/11/20/newscast-101/)

## 🔹 Golang - Go’s Sweet 16
The blog post titled "Go’s Sweet 16" celebrates the 16th anniversary of the Go programming language. It highlights the journey and growth of Go since its inception, including its widespread adoption and the vibrant community that has developed around it. The post reflects on the achievements of the past 16 years and looks forward to future developments and innovations in the Go ecosystem.
👉 [Read more](https://go.dev/blog/16years)

