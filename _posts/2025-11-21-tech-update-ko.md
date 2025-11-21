# 🛠️ 2025-11-21 기술 업데이트 요약

## 🔹 Kubernetes - Ingress NGINX Retirement: What You Need to Know
Ingress NGINX의 은퇴가 발표되었습니다. Kubernetes SIG Network와 보안 대응 위원회는 Ingress NGINX의 유지보수를 2026년 3월까지 진행하며, 이후로는 더 이상의 릴리스, 버그 수정, 보안 취약점 해결 업데이트가 없을 것이라고 밝혔습니다. 현재 배포된 Ingress NGINX는 계속 작동하며 설치 아티팩트도 계속 제공됩니다. 사용자는 Gateway API로의 마이그레이션을 고려하거나 다른 Ingress 컨트롤러로 전환할 것을 권장합니다. Ingress NGINX는 프로젝트의 인기가 높은 반면 유지보수 인력이 부족했으며, 이러한 이유로 프로젝트의 종료가 결정되었습니다. 사용자는 즉시 Gateway API 또는 다른 Ingress 컨트롤러로의 마이그레이션을 시작하는 것이 좋습니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/11/11/ingress-nginx-retirement/)

## 🔹 Spring Boot - A Bootiful Podcast: The legendary Sébastien Deleuze on all that's new and nice in Spring Framework 7
이번 기술 블로그 글은 Spring Framework 7의 새로운 기능에 대해 다룹니다. Spring Boot 4.0의 출시일을 맞아, 이 블로그에서는 Spring Framework의 전설적인 기여자 Sébastien Deleuze와 함께 새로운 기능들을 소개합니다. Spring Initializr(https://start.spring.io)에서 새로운 버전을 확인할 수 있으며, 이번 릴리스에는 많은 새로운 기능들이 포함되어 있습니다.
👉 [자세히 보기](https://spring.io/blog/2025/11/20/a-bootiful-podcast-sebastien-deleuze)

## 🔹 Docker - Docker Model Runner Integrates vLLM for High-Throughput Inference
Docker Model Runner가 vLLM 추론 엔진과 safetensors 모델을 통합하여 고처리량 AI 추론을 가능하게 한다는 블로그 글입니다. Docker Model Runner는 개발자들이 쉽게 모델을 실행하고 실험할 수 있도록 돕기 위해 처음 도입되었으며, 이번 통합을 통해 기존 Docker 도구를 사용하면서도 더 높은 성능을 발휘할 수 있게 되었습니다.
👉 [자세히 보기](https://www.docker.com/blog/docker-model-runner-integrates-vllm/)

## 🔹 Java - Java 26 Warns of Deep Reflection - Inside Java Newscast #101
Java 26에서는 실행 시간에 리플렉션을 통해 final 필드가 변경될 때 경고를 표시합니다. 이는 Java의 무결성을 개선하기 위해 이런 final 필드 변경을 기본적으로 불법화하려는 미래의 변화에 대비하기 위한 것입니다. 이 변화는 유지 보수성, 보안, 성능에 긍정적인 영향을 미칠 것입니다. final 필드 변경을 피하는 것이 권장되지만, 특정 모듈에 대해서는 --enable-final-field-mutation이라는 새로운 영구 명령줄 옵션을 통해 이를 허용할 수 있습니다. 또한, 마이그레이션을 용이하게 하기 위해 보다 일반적이지만 일시적인 옵션인 --illegal-final-field-mutation도 도입되었습니다.
👉 [자세히 보기](https://inside.java/2025/11/20/newscast-101/)

## 🔹 Golang - Go’s Sweet 16
제목: Go의 달콤한 16번째 생일  
요약: 프로그래밍 언어 Go의 16번째 생일을 축하하는 글로, Go 언어의 역사와 발전 과정을 간단히 소개하고 그동안의 성과를 되짚어봅니다. 이 글은 Go 커뮤니티와 개발자들에게 감사의 메시지를 전하며, 앞으로의 발전을 기대합니다.
👉 [자세히 보기](https://go.dev/blog/16years)

