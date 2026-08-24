def main():
    start_worker()


def start_worker():
    print("Starting worker")
    print("Waiting for work")


def process_job(job):
    print("Processing job:", job)


if __name__ == "__main__":
    main()
